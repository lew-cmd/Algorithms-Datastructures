
import unittest
from datetime import date
# helpful information about unittests in python
# https://docs.python.org/3/library/unittest.html
from random import random, randint

from MinHeap import MinHeap as MyHeapPriorityQueue

heap012 = [0, 1, 2]
heap12 = [1, 2]
heap102 = [1, 0, 2]
heap102result = [0, 1, 2]
heap210 = [0, 1, 2]
heap43210 = [0, 1, 2, 3, 4]
heap43210result = [0, 1, 2, 3, 4]
heap43210removeMinResult = [1, 3, 2, 4]
heap0 = [0]

inputLong = [0, 5, 12, 7, 22, 463, 75, 2, 33, 61]
heapLong = [0, 2, 12, 5, 22, 463, 75, 7, 33, 61]


class UnitTestTemplate(unittest.TestCase):
    strCorrection = []

    def setUp(self):
        pass

    def tearDown(self):
        global points
        global maxPoints

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

            # self.strCorrection.append(msg_new)
            self.strCorrection.append("-" + str(
                self.resolve_amount_of_pts_to_deduct(self.resolve_method_name_from_id(self.id()))) + "pts;" +
                                      msg_new + "in test [" + self.resolve_method_name_from_id(
                self.id()) + "]\n" + self.strHorLine)
            # resolve the method name, the corresponding value for deducting points and deduct points
            self.deduct_pts(self.resolve_amount_of_pts_to_deduct(self.resolve_method_name_from_id(self.id())))

        # print(str(date.today()))

    ###############################################
    ################## Test cases##################
    ###############################################

    # ex2 MinHeap

    def test_heap_insert_with_one_element(self):
        heap = MyHeapPriorityQueue()
        for i in heap0:
            heap.insert(i)
        self.assertEqual(heap0, heap.heap, "insert of one element failed was: "+str(heap.heap)+" but should be: "+str(heap0))

    def test_heap_insert_with_upheap_of_middle_element(self):
        heap = MyHeapPriorityQueue()
        for i in heap102:
            heap.insert(i)
        self.assertEqual(heap102result, heap.heap, "insert failed, was: "+str(heap.heap)+" but should be: "+str(heap102result))

    def test_heap_insert_with_upheap_of_last_element(self):
        heap = MyHeapPriorityQueue()
        heap.insert(2)
        heap.insert(3)
        heap.insert(1)

        self.assertEqual(heap.heap[0], 1, "ERROR heap.insert() failed because of wrong element at index 0. was: " + str(
            heap.heap[0]) + ", should be 1 for input sequence [2,3,1]")
        self.assertEqual(heap.heap[1], 3, "ERROR heap.insert() failed because of wrong element at index 1 was: " + str(
            heap.heap[1]) + ", should be 3 for input sequence [2,3,1]")
        self.assertEqual(heap.heap[2], 2, "ERROR heap.insert() failed because of wrong element at index 2 was: (" + str(
            heap.heap[2]) + ", should be 2 for input sequence [2,3,1]")

    def test_heap_insert_without_upheap(self):
        heap = MyHeapPriorityQueue()
        for i in heap012:
            heap.insert(i)

        self.assertEqual(heap012, heap.heap, "insert failed, was: "+str(heap.heap)+" but should be: "+str(heap012))

    def test_heap_insert_with_multiple_upheap(self):
        heap = MyHeapPriorityQueue()
        for i in heap43210:
            heap.insert(i)

        self.assertEqual(heap43210result, heap.heap, "insert failed, was: "+str(heap.heap)+" but should be: "+str(heap43210result))

    def test_heap_insert_with_init_cap_1_with_doubling_cap(self):
        heap = MyHeapPriorityQueue()
        for i in heap43210:
            heap.insert(i)

        self.assertEqual(heap43210result, heap.heap, "insert failed with init capacity 1, was: "+str(heap.heap)+" but should be: "+str(heap43210result))

    def test_heap_insert_none(self):
        heap = MyHeapPriorityQueue()
        ex = None
        try:
            heap.insert(None)
        except ValueError as ve:
            ex = ve
        self.assertTrue(isinstance(ex, ValueError),
                        "ERROR: heap.insert() did not raise an exception when trying to insert None")

    def test_heap_is_empty(self):
        heap = MyHeapPriorityQueue()
        self.assertTrue(heap.is_empty(), "ERROR: heap.is_empty() -> returned False. The heap should have been empty (return True), but it returned False.")

        heap.insert(1)
        self.assertFalse(heap.is_empty(), "ERROR: heap.is_empty() -> The heap should not have been empty, but it is.")

    def test_heap_get_min(self):
        heap = MyHeapPriorityQueue()
        heap.insert(10)
        self.assertEqual([10], heap.heap, "get_min cannot be tested because insert created an invalid heap: "+str(heap.heap)+" but should be: "+str([10]))
        self.assertEqual(heap.get_min(), 10, "ERROR: heap.get_min() returned incorrect value (" + str(
            heap.get_min()) + ") for insert sequence [10], should be 10")

    def test_heap_get_min_with_multiple_elements(self):
        heap = MyHeapPriorityQueue()
        for i in heap43210:
            heap.insert(i)
        self.assertEqual(heap43210result, heap.heap, "get_min cannot be tested because insert created an invalid heap: "+str(heap.heap)+" but should be: "+str(heap43210result))
        self.assertEqual(heap.get_min(), 0, "ERROR: heap.get_min() returned incorrect value (" + str(
            heap.get_min()) + ") for insert sequence " + str(heap43210) + ", should be 0")

    def test_heap_get_min_empty_heap(self):
        heap = MyHeapPriorityQueue()
        self.assertIsNone(heap.get_min(), "ERROR: get_min of empty heap returned "+str(heap.get_min())+" should be 0")

    def test_heap_remove_min_last_element(self):
        heap = MyHeapPriorityQueue()
        for i in heap0:
            heap.insert(i)
        self.assertEqual(heap0, heap.heap,
                                   "get_min cannot be tested because insert created an invalid heap: " + str(
                                       heap.heap) + " but should be: " + str(heap0))
        self.assertEqual(heap.remove_min(), 0, "ERROR: heap.remove_min() returned incorrect value (" + str(
            heap.remove_min()) + ") for insert sequence " + str(heap0) + ", should be 0")

    def test_heap_remove_min_without_downheap(self):
        heap = MyHeapPriorityQueue()
        for i in heap012:
            heap.insert(i)
        self.assertEqual(heap012, heap.heap,
                                   "get_min cannot be tested because insert created an invalid heap: " + str(
                                       heap.heap) + " but should be: " + str(heap012))
        min_rem = heap.remove_min()
        self.assertEqual(min_rem, 0, "ERROR: heap.remove_min() returned incorrect value (" + str(
            min_rem) + ") for insert sequence " + str(heap012) + ", should be 0")
        self.assertEqual(heap12, heap.heap, "remove_min failed, was: "+str(heap.heap)+" but should be: "+str(heap12))

    def test_heap_remove_min_with_downheap(self):
        heap = MyHeapPriorityQueue()
        for i in heap43210:
            heap.insert(i)
        self.assertEqual(heap43210result, heap.heap,
                                   "get_min cannot be tested because insert created an invalid heap: " + str(
                                       heap.heap) + " but should be: " + str(heap43210result))
        min_rem = heap.remove_min()
        self.assertEqual(min_rem, 0, "ERROR: heap.remove_min() returned incorrect value (" + str(
            min_rem) + ") for insert sequence " + str(heap43210removeMinResult) + ", should be 0")
        self.assertEqual(heap43210removeMinResult, heap.heap, "remove_min failed, was: "+str(heap.heap)+" but should be: "+str(heap43210removeMinResult))

    def test_heap_size_with_insert_and_remove(self):
        heap = MyHeapPriorityQueue()
        self.assertEqual(0, heap.get_size(), "ERROR: get_size returned "+str(heap.get_size())+" for empty heap but should be 0")
        heap.insert(2)
        self.assertEqual(1, heap.get_size(),
                         "ERROR: get_size returned " + str(heap.get_size()) + " for heap after one insert but should be 1")
        heap.insert(2)
        self.assertEqual(2, heap.get_size(),
                         "ERROR: get_size returned " + str(heap.get_size()) + " for heap after two inserts but should be 2")
        heap.remove_min()
        self.assertEqual(1, heap.get_size(),
                         "ERROR: get_size returned " + str(heap.get_size()) + " for heap after remove of one element but should be 1")
        heap.remove_min()
        self.assertEqual(0, heap.get_size(),
                         "ERROR: get_size returned " + str(heap.get_size()) + " for empty heap after last remove_min but should be 0")



    ####################################################
    # help methods
    ####################################################

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    def resolve_method_name_from_id(self, argument):
        idx = self.id().rfind('.')
        # print("****"+self.id()[idx+1:])
        return self.id()[idx + 1:]

    def _to_set(self, list):
        res = []
        for l in list:
            if l is not None:
                res.append(l)
        return res


if __name__ == "__main__":
    unittest.main()
