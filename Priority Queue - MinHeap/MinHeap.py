
class MinHeap:

    def __init__(self):
        self.heap = []
        self.size = -1

    def get_heap(self):
        """for testing purposes only
        """
        return self.heap

    def insert(self, integer_val: int) -> None: #push
        """inserts integer_val into the min heap
        @param integer_val: the value to be inserted
        @raises ValueError if integer_val is None
        """
        if not isinstance(integer_val, int):
            raise ValueError

        self.heap.append(integer_val)
        self.size += 1
        self.up_heap(self.size)

    def is_empty(self) -> bool:
        """returns True if the min heap is empty, False otherwise
        @return True or False
        """
        if self.heap:
            return False
        else:
            return True

    def get_min(self) -> int:
        """returns the value of the minimum element of the PQ without removing it
        @return the minimum value of the PQ or None if no element exists
        """
        if len(self.heap) > 0:
            return min(self.heap[:self.size+1])
        else:
            return None

    def remove_min(self) -> int: #pop
        """removes the minimum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """

        if self.is_empty():
            return None
        else:
            root = self.heap[0]

            self.heap[0] = self.heap[len(self.heap)-1]

            #self.size -= 1

            *self.heap, _ = self.heap  #update heap withouth the last element

            self.down_heap(0)

            return root

    def get_size(self) -> int:
        """returns the number of elements in the PQ
        @return number of elements
        """
        return len(self.heap)

    def up_heap(self, index):
        while index > 0:
            if self.heap[index] < self.heap[self.parent(index)]:
                self.swap(index, self.parent(index))
            index = self.parent(index)

    def sift_down(self, index):
        i = index
        left = self.left_child(i)
        right = self.right_child(i)

        # if current index/node has at least one child
        while(i*2) < self.size:
            # get index of min child
            min = left if right >= self.size or self.heap[left] <= self.heap[right] else right
            # swap values of current element is greater than its min child
            if self.heap[i] > self.heap[min]:
                self.swap(i, min)
            i = min

    def down_heap(self, index):
        while self.left_child(index) <= self.size-1:
            smaller_child_index = self.get_min_child(index)
            child = self.heap[smaller_child_index]
            parent = self.heap[index]
            if parent > child:
                self.heap[index] = child
                self.heap[smaller_child_index] = parent
            index = smaller_child_index
            if self.get_min() == min(self.heap[:self.size]):
                break

    def parent(self, index) -> int:
        return (index-1)//2

    def left_child(self, index) -> int:
        return (index * 2) + 1

    def right_child(self, index) -> int:
        return (index * 2) + 2

    def get_min_child(self, index) -> int:
        i = index
        # if node at index has only one child, return index of the same
        if (i * 2) + 1 > self.size:
            return i * 2
        else:
            # otherwise, two children
            if self.left_child(i) < self.right_child(i):
                return self.left_child(i)
            else:
                return self.right_child(i)

    def swap(self, index1, index2) -> int:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    """recommended Methods 
     up_heap(index) 
     down_heap(index) 
     parent(index) 
     left_child(index) 
     right_child(index) 
     swap(index1, index2)
     
    remove_min failed, was: [1, 2, 4, 3] but should be: [1, 3, 2, 4]
    [1, 2, 4, 3] != [1, 3, 2, 4]

    Expected :[1, 3, 2, 4]
    Actual   :[1, 2, 4, 3]
     """
