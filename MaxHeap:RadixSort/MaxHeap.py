class MaxHeap:
    def __init__(self, list):
        """
        @param list from which the heap should be created
        @raises ValueError if list is None.
        Creates a bottom-up maxheap in place.
        """
        self.heap = None
        self.size = 0
        # TODO
        if list is None:
            raise ValueError

        self.heap = list
        self.size = len(list)
        last_idx = self.size - 1
        right_parent_idx = (last_idx -1)//2
        for i in range(right_parent_idx, -1,-1):
            self.down_heap(i)

    def down_heap(self, index): #taken from ex.5, just changed equalities and min to max
        max_child = self.bigger_child(index) #get the bigger child or None
        if max_child is not None: #if there is at least one child
            child = self.heap[max_child]
            parent = self.heap[index]
            if child > parent: #check if child is bigger than parent, and swap nodes
                self.heap[index] = child
                self.heap[max_child] = parent
                self.down_heap(max_child) #repeat until the node has a child, until you reach the bottom of the tree

    def get_heap(self):
        # helper function for testing, do not change
        return self.heap

    def get_size(self):
        """
        @return size of the max heap
        """
        return self.size

    def contains(self, val):
        """
        @param val to check if it is contained in the max heap
        @return True if val is contained in the heap else False
        @raises ValueError if val is None.
        Tests if an item (val) is contained in the heap. Do not search the entire array sequentially, but use the properties of a heap
        """
        # TODO
        if val is None:
            raise ValueError
        if self.is_empty():
            return False
        else:
            i = 0
            a = self.search_help(val,i)
            return a == True

    def search_help(self,val,index):
        if self.heap[index]==val:
            return True
        left_idx, right_idx = self.left_child(index), self.right_child(index)

        if right_idx < self.get_size() and self.heap[right_idx] >= val:
            res = self.search_help(val, right_idx)
            if res:
                return True

        if left_idx < self.get_size() and self.heap[left_idx] >= val:
            res = self.search_help(val, left_idx)
            if res:
                return True

    def is_empty(self):
        """
        @return True if the heap is empty, False otherwise
        """
        return self.get_size() == 0

    def remove_max(self):
        """
        Removes and returns the maximum element of the heap
        @return maximum element of the heap or None if heap is empty
        """
        #TODO

        if self.is_empty():
            return None
        else:
            value = max(self.heap[:self.size]) #find max value of tree, its a root
            self.heap[0] = self.heap[self.size - 1] #the root will become the node from tail
            self.heap[self.size - 1] = None #the last node changed to None
            self.size -= 1 #decrease size of heap
            self.heap = self.heap[:-1] #delete the None from heap
            if self.size > 1: #if the heap has more than 1 element, down_heap
                self.down_heap(0)

            if self.size == 1: #if the heap has exactly one elemenet, return it
                return value

            return value

    def sort(self):
        """
        This method sorts (ascending) the list in-place using HeapSort, e.g. [1,3,5,7,8,9]
        """
        if self.get_size() == 1:
            pass
        else:
            last_index = self.get_size() - 1
            for _ in range(self.get_size()):
                first_index, last_index = 0, last_index
                self.swap(index1=first_index, index2=last_index)
                heap_length = last_index - 1
                last_index -= 1
                self.down_heap_sort(0, heap_length)


    def left_child_sort(self, index, largest):
        left_index = 2 * index + 1
        if left_index > largest:
            return None
        else:
            return left_index

    def right_child_sort(self, index, largest):
        right_index = 2 * index + 2
        if right_index > largest:
            return None
        else:
            return right_index


    def bigger_child(self, index: int) -> int:
        left_node = self.left_child(index)
        right_node = self.right_child(index)
        # Check if there is a left node.
        if left_node > self.size - 1:  # check if left node is none, if yes return None as there cant be right node
            return None
        elif right_node > self.size - 1:  # check if there is right node, if not we can return left_node
            return left_node
        else:  # if there is right and left node, choose the smaller one
            if self.heap[left_node] < self.heap[right_node]:
                return right_node
            else:
                return left_node

    def down_heap_sort(self, index, largest):
        parent_element = self.heap[index]
        left_index, right_index = self.left_child_sort(index, largest), self.right_child_sort(index, largest)
        if left_index == None or right_index == None:
            child_index = left_index or right_index
        else:
            left_element, right_element = self.heap[left_index], self.heap[right_index]
            if left_element >= right_element:
                child_index = left_index
            else:
                child_index = right_index
        if child_index:
            child_element = self.heap[child_index]
        else:
            # when child element does not exist,
            child_element = parent_element - 1
        while child_index and parent_element < child_element:
            self.swap(index, child_index)
            index = child_index
            parent_element = self.heap[index]
            left_index, right_index = self.left_child_sort(index, largest), self.right_child_sort(index,
                                                                                                            largest)
            if left_index == None or right_index == None:
                child_index = left_index or right_index
            else:
                left_element, right_element = self.heap[left_index], self.heap[right_index]
                if left_element >= right_element:
                    child_index = left_index
                else:
                    child_index = right_index
            if child_index:
                child_element = self.heap[child_index]
            else:
                # when child element does not exist,
                child_element = parent_element - 1

        # helping functions to find children and parents
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

    def swap(self, index1, index2):
        elem_ind_1, elem_ind_2 = self.heap[index1], self.heap[index2]
        self.heap[index1] = elem_ind_2
        self.heap[index2] = elem_ind_1