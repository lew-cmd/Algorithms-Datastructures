from typing import List, Tuple
import string

# Using constants might make this more readable.
START = 'S'
EXIT = 'X'
VISITED = '.'
OBSTACLE = '#'
PATH = ' '


class Maze:
    """Maze object, used for demonstrating recursive algorithms."""

    def __init__(self, maze_str: str):
        """Initialize Maze.

        Args:
            maze_str (str): Maze represented by a string, 
            where rows are separated by newlines (\n).

        Raises:
            ValueError, if maze_str is invalid, i.e. if it is not the correct type, 
            if any of its dimensions is less than three, or if it contains
[            characters besides {'\n', ' ', '*'}.
        """
        # We internally treat this as a List[List[str]], as it makes indexing easier.
        self._maze = list(list(row) for row in maze_str.splitlines())

        self._exits: List[Tuple[int, int]] = []
        self._max_recursion_depth = 0
        # TODO: Adjust to raise ValueError

        if not isinstance(maze_str, str) or not maze_str:
            raise ValueError

        self._x = len(self._maze)
        self._y = len(self._maze[1])

        if self._x  < 3 or self._y < 3:
            raise ValueError

        #check if any character exists besides '\n', ' ', '*'
        SET = set(string.printable)
        SET.remove('#')
        SET.remove(' ')
        SET.remove('\n')

        for maze in self._maze:
            if SET in maze:
                raise ValueError


    def find_exits(self, start_row: int, start_col: int, depth: int = 0) -> bool:
        """Find and save all exits into `self._exits` using recursion, save 
        the maximum recursion depth into 'self._max_recursion_depth' and mark the maze.

        An exit is an accessible from S empty cell on the outer rims of the maze.

        Args:
            start_row (int): row to start from. 0 represents the topmost cell.
            start_col (int): column to start from; 0 represents the leftmost cell.
            depth (int): Depth of current iteration.

        Raises:
            ValueError: If the starting position is out of range or not walkable path.
        """

        if start_row > self._x-1 or start_col > self._y-1:
            raise ValueError

        location = (start_row, start_col)
        maze_x_val = self._maze[location[0]]
        maze_temp = self._maze

        #set S(tart) marker
        if depth == 0:
            maze_x_val = self.change_field_val(maze_x_val, location, 'S')
        #or place '.'
        else:
            maze_x_val = self.change_field_val(maze_x_val, location, '.')

        valid_moves = self.check_surroundings(location)

        #checking for exits
        if (location[0] == 0 or         #north
            location[0] == self._x-1 or   #south
            location[1] == self._y-1 or   #east
            location[1] == 0):          #west

            self._exits.append(location)
            maze_x_val = self.change_field_val(maze_x_val, location, 'X')

        #update depth
        if depth > self.max_recursion_depth:
            self._max_recursion_depth = depth

        #update maze
        maze_temp[location[0]] = maze_x_val
        self._maze = maze_temp

        #calling find_exits recursively as long as there are valid moves
        if len(valid_moves) > 0:
            depth += 1
            for move in valid_moves:
                self.find_exits(move[0], move[1], depth)

        if len(self._exits) > 0:
            return True
        else:
            return False

    def change_field_val(self, maze_x_val, location, value):
        maze_x_val = maze_x_val[:location[1]] + list(value) + maze_x_val[location[1]+1:]
        return maze_x_val

    def check_surroundings(self, location: list):
        valid_moves = []
        location = list(location)

        # check south
        if location[0] < self._x-1:
            south_val = self._maze[location[0] + 1][location[1]]
            if south_val == ' ':
                south = [location[0] + 1, location[1]]
                valid_moves.append(south)

         # check east
        if location[1] < self._y-1:
            east_val = self._maze[location[0]][location[1] + 1]
            if east_val == ' ':
                east = [location[0], location[1] + 1]
                valid_moves.append(east)

        #check north
        if location[0] > 0:
            north_val = self._maze[location[0]-1][location[1]]
            if north_val == ' ':
                north = [location[0]-1, location[1]]
                valid_moves.append(north)

        #check west
        if location[1] > 0:
            west_val = self._maze[location[0]][location[1]-1]
            if west_val == ' ':
                west = [location[0], location[1]-1]
                valid_moves.append(west)

        return valid_moves

    @property
    def exits(self) -> List[Tuple[int, int]]:
        """List of tuples of (row, col)-coordinates of currently found exits."""
        return self._exits

    @property
    def max_recursion_depth(self) -> int:
        """Return the maximum recursion depth after executing find_exits()."""
        return self._max_recursion_depth

    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._maze)

    __repr__ = __str__
