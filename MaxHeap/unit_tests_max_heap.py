import unittest
from datetime import date
# helpful information about unittests in python
# https://docs.python.org/3/library/unittest.html
from random import random, randint

from MaxHeap import MaxHeap


heap0 = [0]
heap012 = [2,1,0]
heap102 = [1, 0, 2]
heap102solution1 = [0, 1, 2]
heap102solution2 = [2,0,1]
heap43210 = [4, 3, 2, 1, 0]
test_array = [3, 9, 17, 2, 23, 1, 5, 4, 19, 17, 7, 18, 8, 67, 6, 11, 0]
test_array_sorted=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 17, 17, 18, 19, 23, 67]

#test_array_sorted = [67, 23, 19, 18, 17, 17, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
testArray2 = [6, 5, 6, 15, 4, 7, 20, 16]
testArray3 = [3, 9, 5, 4, 0]


class UnitTestTemplate(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        if hasattr(self, '_outcome'):  # Python 3.4+
            result = self.defaultTestResult()  # these 2 methods have no side effects
            self._feedErrorsToResult(result, self._outcome.errors)
        else:  # Python 3.2 - 3.3 or 3.0 - 3.1 and 2.7
            result = getattr(self, '_outcomeForDoCleanups', self._resultForDoCleanups)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure

        # demo:   report short info immediately (not important)
        if not ok:
            typ, text = ('ERROR', error) if error else ('FAIL', failure)
            # msg = [x for x in text.split('\n')[1:] if not x.startswith(' ')][0]
            # print("\n[%s:] {%s}\n     (%s)" % (typ, self.id(), msg))
            # msg = msg.split('\'')[1]
            # add error message to list for later output to file
            text = text.split("Error: ")[1:]
            msg_new = ""
            if len(text[1:]) != 0:
                for m in text[1:]:
                    msg_new += m.split("::")[0]
            else:
                for m in text:
                    msg_new += m
            msg_new = msg_new.replace("False is not true : ", " ")
            msg_new = msg_new.replace("None is not true : ", " ")
            msg_new = msg_new.replace("' is not None", " ")


    ###############################################
    ################## Test cases##################
    ###############################################

    # ex1 linked list

    def test_heap_bottom_up_with_arr_one_element(self):
        heap = MaxHeap(heap0.copy())
        heap_arr = heap.get_heap()
        self.assertEqual(1, heap.get_size(),
                         "ERROR: BottumUp construction of heap with input array {0} failed, incorrect size")
        self.assertEqual(heap0[0], heap_arr[0],
                         "ERROR: BottumUp construction of heap with input array {0} failed, incorrect element")


    def test_heap_bottom_up_with_arr_without_downheap(self):
        heap = MaxHeap(heap012.copy())
        heap_arr = heap.get_heap()
        self.assertEqual(len(heap012), heap.get_size(),
                         "ERROR: BottumUp construction of heap with input array " + str(heap012) + " returned wrong size")
        for i in range(0, len(heap012)):
            self.assertEqual(heap012[i], heap_arr[i], "ERROR: BottumUp construction of heap with input array " + str(
                heap012) + " had wrong element at index " + str(i))

    def test_heap_bottom_up_with_arr_with_single_downheap(self):
        heap = MaxHeap(heap102.copy())
        heap_arr = heap.get_heap()
        res = False

        if heap_arr == heap102solution1 or heap_arr == heap102solution2:
            res = True

        self.assertTrue(res, "ERROR: heap with input sequence "+str(heap102)+ " was not created correctly")

    def test_heap_bottom_up_with_arr_with_multiple_downheap(self):
        heap = MaxHeap(heap43210.copy())
        print(heap.heap)
        self.assertEqual(len(heap43210), heap.get_size(),
                         "ERROR: BottumUp construction of heap with input array " + str(heap43210) + " returned wrong size")
        self.assertTrue(self._test_heap_structure(heap.get_heap(), 4),
                        "ERROR: BottumUp construction of heap with input array " + str(
                            heap43210) + " had an incorrect heap structure")

    def test_heap_bottom_up_init_with_none(self):
        ex = None
        try:
            heap = MaxHeap(None)
        except ValueError as ve:
            ex = ve
        self.assertTrue(isinstance(ex, ValueError), "ERROR: calling init of heap with None did not raise an exception")

    def test_heap_bottom_up_construction_large(self):
        heap = MaxHeap(test_array.copy())
        self.assertEqual(len(test_array), heap.get_size(),
                         "ERROR: BottumUp construction of heap with input array " + str(test_array) + " returned wrong size")
        self.assertTrue(self._test_heap_structure(heap.get_heap(), 67),
                        "ERROR: BottumUp construction of heap with input array " + str(
                            test_array) + " had an incorrect heap structure")

    def test_heap_bottom_up_remove_Max_last_element(self):
        heap = MaxHeap(heap0.copy())
        self.assertEqual(0, heap.remove_max(),
                         "ERROR: remove_Max returned incorrect element for input sequence " + str(heap0))

    def test_heap_bottom_up_remove_Max_without_downheap(self):
        heap = MaxHeap(heap012.copy())
        self.assertEqual(len(heap012), heap.get_size(),
                         "ERROR: remove_Max could not be tested because heap could not be created using input sequence " + str(
                             heap012))
        self.assertTrue(self._test_heap_structure(heap.get_heap(), 2),
                        "ERROR: remove_Max could not be tested because heap could not be created using input sequence " + str(
                            heap012))

        self.assertEqual(2, heap.remove_max(),
                         "ERROR: remove_Max returned incorrect element for input sequence " + str(heap012))

        self.assertEqual(len(heap012) - 1, heap.get_size(),
                         "ERROR: heap has an incorrect size after remove_Max with input sequence " + str(heap012))
        self.assertTrue(self._test_heap_structure(heap.get_heap(), 2),
                        "ERROR: heap has an incorrect size after remove_Max with input sequence " + str(heap012))

    def test_heap_bottom_up_remove_Max_with_downheap(self):
        heap = MaxHeap(heap43210.copy())
        self.assertEqual(len(heap43210), heap.get_size(), "ERROR: remove_Max could not be tested because heap could not be created using input sequence "+str(heap43210))
        self.assertTrue(self._test_heap_structure(heap.get_heap(), 4), "ERROR: remove_Max could not be tested because heap could not be created using input sequence "+str(heap43210))

        self.assertEqual(4, heap.remove_max(),
                         "ERROR: remove_Max returned incorrect element for input sequence " + str(heap43210))
        self.assertEqual(len(heap43210) - 1, heap.get_size(),
                         "ERROR: heap has an incorrect size after remove_Max with input sequence " + str(heap43210))


    def test_heap_bottom_up_contains_existing(self):
        heap = MaxHeap(test_array.copy())
        self.assertTrue(heap.contains(3), "ERROR: contains returned False for element 3 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(9), "ERROR: contains returned False for element 9 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(17), "ERROR: contains returned False for element 17 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(2), "ERROR: contains returned False for element 2 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(23), "ERROR: contains returned False for element 23 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(1), "ERROR: contains returned False for element 1 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(5), "ERROR: contains returned False for element 5 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(4), "ERROR: contains returned False for element 4 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(19), "ERROR: contains returned False for element 19 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(17), "ERROR: contains returned False for element 17 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(7), "ERROR: contains returned False for element 7 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(18), "ERROR: contains returned False for element 18 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(8), "ERROR: contains returned False for element 8 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(67), "ERROR: contains returned False for element 67 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(6), "ERROR: contains returned False for element 6 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(11), "ERROR: contains returned False for element 11 using input sequence "+str(test_array))
        self.assertTrue(heap.contains(0), "ERROR: contains returned False for element 0 using input sequence "+str(test_array))

    def test_heap_bottom_up_contains_not_existing(self):
        heap = MaxHeap(test_array.copy())
        self.assertFalse(heap.contains(44), "ERROR: contains returned True for element 44 using input sequence "+str(test_array))
        self.assertFalse(heap.contains(-1), "ERROR: contains returned True for element -1 using input sequence "+str(test_array))
        self.assertFalse(heap.contains(10), "ERROR: contains returned True for element 10 using input sequence "+str(test_array))
        self.assertFalse(heap.contains(13), "ERROR: contains returned True for element 13 using input sequence "+str(test_array))
        self.assertFalse(heap.contains(102), "ERROR: contains returned True for element 102 using input sequence "+str(test_array))
        self.assertFalse(heap.contains(3489), "ERROR: contains returned True for element 3489 using input sequence "+str(test_array))

    def test_heap_bottom_up_sort(self):
        tmp = test_array.copy()
        heap = MaxHeap(tmp)
        heap.sort()
        print(heap.heap)
        print(test_array_sorted)
        self.assertEqual(len(tmp), len(test_array_sorted), "ERROR: sort failed because of incorrect list size")
        for i in range(0, len(test_array_sorted)):
            self.assertEqual(test_array_sorted[i], tmp[i], "ERROR: sort failed with input sequence "+str(test_array)+" at index "+str(i))


    ####################################################
    # help methods
    ####################################################

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    def _test_heap_structure(self, heap, index):
        try:
            children = self.children(heap, index)
            if len(children) <= 0:
                return True
            if heap[children[0]] - heap[index] < 0:
                return False
            if len(children) <= 1:
                return True
            if heap[children[1]] - heap[index] < 0:
                return False
            return self._test_heap_structure(heap, children[0]) and self._test_heap_structure(heap, children[1])
        except:
            return False

    def children(self, heap, index):
        index += 1
        c1 = 2 * index - 1
        c2 = 2 * index
        if c1 > len(heap) - 1:
            return []
        if c2 > len(heap) - 1:
            return [c1]
        return [c1, c2]



if __name__ == "__main__":
    unittest.main()
