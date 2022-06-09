class MinHeap:

    def __init__(self):
        self.heap = []
        self.size = len(self.heap)

    def get_heap(self):
        """for testing purposes only
        """
        return self.heap

    def insert(self, integer_val: int) -> None:
        """inserts integer_val into the min heap
        @param integer_val: the value to be inserted
        @raises ValueError if integer_val is None
        """
        # TODO
        if integer_val is None:
            raise ValueError('integer_val is None')
        self.heap.append(integer_val)
        self.size += 1
        self.up_heap(self.size - 1)

    def up_heap(self, index):
        while index > 0:
            if self.heap[index] < self.heap[self.parent(index)]:  #if parent is bigger, swap the nodes
                temp = self.heap[self.parent(index)]
                self.heap[self.parent(index)] = self.heap[index]
                self.heap[index] = temp
            index = self.parent(index)  # move index to the parent

    def is_empty(self) -> bool:
        """returns True if the min heap is empty, False otherwise
        @return True or False
        """
        # TODO
        if self.size == 0:
            return True
        else:
            return False

    def get_min(self) -> int:
        """returns the value of the minimum element of the PQ without removing it
        @return the minimum value of the PQ or None if no element exists
        """
        # TODO
        if self.is_empty():
            return None
        else:
            return min(self.heap[:self.size])

    def remove_min(self) -> int:
        """removes the minimum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """
        # TODO

        if self.is_empty():
            return None
        else:
            value = min(self.heap[:self.size]) #find min value of tree, its a root
            self.heap[0] = self.heap[self.size - 1] #the root will become the node from tail
            self.heap[self.size - 1] = None #the last node changed to None
            self.size -= 1 #decrease size of heap
            self.heap = self.heap[:-1] #delete the None from heap
            if self.size > 1: #if the heap has more than 1 element, down_heap
                self.down_heap(0)

            if self.size == 1: #if the heap has exactly one elemenet, return it
                return value

            return value

    def down_heap(self, index):
        min_child = self.smaller_child(index) #get the smaller child or None
        if min_child is not None: #if there is at least one child
            child = self.heap[min_child]
            parent = self.heap[index]
            if child < parent: #check if child is smaller than parent, and swap nodes
                self.heap[index] = child
                self.heap[min_child] = parent
                self.down_heap(min_child) #repeat until the node has a child, until you reach the bottom of the tree

    def smaller_child(self, index: int) -> int:
        left_node = self.left_child(index)
        right_node = self.right_child(index)
        # Check if there is a left node.
        if left_node > self.size - 1:  # check if left node is none, if yes return None as there cant be right node
            return None
        elif right_node > self.size - 1:  # check if there is right node, if not we can return left_node
            return left_node
        else:  # if there is right and left node, choose the smaller one
            if self.heap[left_node] < self.heap[right_node]:
                return left_node
            else:
                return right_node

    def get_size(self) -> int:
        """returns the number of elements in the PQ
        @return number of elements
        """
        # TODO
        return self.size

#helping functions to find children and parents 
    def left_child(self, index):
        return (index * 2) + 1

    def right_child(self, index):
        return (index * 2) + 2

    def parent(self, index):
        # for odd values
        if (index % 2) == 1:
            return index // 2
        # for even values
        if (index % 2) == 0:
            return (index - 1) // 2

