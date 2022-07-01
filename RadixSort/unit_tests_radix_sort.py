import unittest

from datetime import date

# helpful information about unittests in python

# https://docs.python.org/3/library/unittest.html

from random import random, randint



from RadixSort import RadixSort


#    Integer testArrayBase10[] = {33, 614, 10216, 2123, 21523, 164504, 5142, 412, 161, 17125, 2231, 2123, 22, 6411, 21, 1123515, 0};
#    Integer testArrayBase7[] = {33, 614, 10216, 2123, 21523, 164504, 5142, 412, 161, 16125, 2231, 2123, 22, 6411, 21, 1123515, 0};#
#    Integer testArrayIterationBase10[] = {33, 614, 10216, 2123, 21523, 164504, 5142, 402, 6411, 21, 1123515, 0};
#    Integer testArrayIterationBase7[] = {33, 614, 10216, 2123, 21523, 164504, 5142, 402, 6311, 21, 1123515, 0};


#test_array = [33, 614, 10216, 2123, 21523, 164504, 5142, 412, 161, 16125, 2231, 2123, 22, 6411, 21, 1123515, 0]

#test_array_iteration = [33, 614, 10216, 2123, 21523, 164504, 5142, 402, 6411, 21, 1123515, 0]

test_array_equals = [111, 4, 4, 4]

test_array_presorted = [0,12,15,234,5562]

#set the base of array
base=7

if(base==7):
    test_array=[33, 614, 10216, 2123, 21523, 164504, 5142, 412, 161, 16125, 2231, 2123, 22, 6411, 21, 1123515, 0]

    test_array_iteration=[33, 614, 10216, 2123, 21523, 164504, 5142, 402, 6411, 21, 1123515, 0]
elif (base==10):
    test_array=[33, 914, 17216, 2123, 21123, 164584, 5142, 412, 191, 17125, 2231, 2123, 22, 6711, 21, 1123515,0]
    test_array_iteration=[33, 914, 17216, 2123, 21123, 164584, 5142, 402, 6711, 21, 1123515, 0]



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



    def test_radix_sort_result(self):

        result = None

        r = RadixSort()

        result = r.sort(test_array.copy())

        test_array.sort(reverse=True)

        for i in range(0, len(test_array)):

            self.assertEqual(test_array[i], result[i],

                             "ERROR: sort with input sequence " + str(test_array) + " failed at index " + str(

                                 i) + ": " + str(result))



    def test_radix_sort_result_one_element(self):

        result = None

        r = RadixSort()

        result = r.sort([1])

        self.assertEqual(1, result[0], "ERROR: sort with input sequence " + str(test_array) + " failed at index " + str(

            1) + ": " + str(result))

        self.assertEqual(1, len(result),

                         "ERROR: sort with input sequence " + str(test_array) + " failed because of incrroect size")



    def test_radix_sort_equal_elements(self):

        result = None

        r = RadixSort()

        result = r.sort(test_array_equals.copy())

        test_array_equals.sort(reverse=True)

        for i in range(0, len(test_array_equals)):

            self.assertEqual(test_array_equals[i], result[i],

                             "ERROR: sort with input sequence " + str(test_array) + " failed at index " + str(

                                 i) + ": " + str(result))



    def test_radix_sort_presorted_array(self):

        result = None

        r = RadixSort()

        result = r.sort(test_array_presorted.copy())

        test_array_presorted.sort(reverse=True)

        for i in range(0, len(test_array_presorted)):

            self.assertEqual(test_array_presorted[i], result[i],

                             "ERROR: sort with input sequence " + str(test_array) + " failed at index " + str(

                                 i) + ": " + str(result))



    def test_radix_sort_bucket_lists_iteration1(self):

        bucket_list_history = None

        it_idx = 0

        err_msg = "Radix sort of input array " + str(test_array_iteration) + " failed in iteration " + str(

            it_idx + 1) + " on"

        r = RadixSort()

        result = r.sort(test_array_iteration.copy())

        bucket_list_history = r.get_bucket_list_history()



        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")
        print(len(bucket_list_history[it_idx]))

        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,

                        "ERROR: bucket_list_history[" + str(it_idx) + "] is of wrong size, must contain 7 buckets")



        self.assertEqual(1, len(bucket_list_history[it_idx][0]), err_msg + " bucket 0 because of wrong size")

        self.assertTrue(0 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 0")



        self.assertEqual(2, len(bucket_list_history[it_idx][1]), err_msg + " bucket 1 because of wrong size")

        self.assertTrue(6411 in bucket_list_history[it_idx][1], err_msg + " bucket 0 because of missing element 6411")

        self.assertTrue(21 in bucket_list_history[it_idx][1], err_msg + " bucket 0 because of missing element 21")



        self.assertEqual(2, len(bucket_list_history[it_idx][2]), err_msg + " bucket 2 because of wrong size")

        self.assertTrue(5142 in bucket_list_history[it_idx][2], err_msg + " bucket 0 because of missing element 5142")

        self.assertTrue(402 in bucket_list_history[it_idx][2], err_msg + " bucket 0 because of missing element 402")



        self.assertEqual(3, len(bucket_list_history[it_idx][3]), err_msg + " bucket 3 because of wrong size")

        self.assertTrue(33 in bucket_list_history[it_idx][3], err_msg + " bucket 0 because of missing element 33")

        self.assertTrue(2123 in bucket_list_history[it_idx][3], err_msg + " bucket 0 because of missing element 2123")

        self.assertTrue(21523 in bucket_list_history[it_idx][3], err_msg + " bucket 0 because of missing element 21523")



        self.assertEqual(2, len(bucket_list_history[it_idx][4]), err_msg + " bucket 4 because of wrong size")

        self.assertTrue(614 in bucket_list_history[it_idx][4], err_msg + " bucket 0 because of missing element 614")

        self.assertTrue(164504 in bucket_list_history[it_idx][4],

                        err_msg + " bucket 0 because of missing element 164504")



        self.assertEqual(1, len(bucket_list_history[it_idx][5]), err_msg + " bucket 5 because of wrong size")

        self.assertTrue(1123515 in bucket_list_history[it_idx][5],

                        err_msg + " bucket 0 because of missing element 1123515")



        self.assertEqual(1, len(bucket_list_history[it_idx][6]), err_msg + " bucket 6 because of wrong size")

        self.assertTrue(10216 in bucket_list_history[it_idx][6], err_msg + " bucket 0 because of missing element 10216")



    def test_radix_sort_bucket_lists_iteration2(self):

        bucket_list_history = None

        it_idx = 1

        err_msg = "Radix sort of input array " + str(test_array_iteration) + " failed in iteration " + str(

            it_idx + 1) + " on"

        r = RadixSort()

        result = r.sort(test_array_iteration.copy())

        bucket_list_history = r.get_bucket_list_history()



        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")

        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,

                        "ERROR: bucket_list_history[" + str(it_idx) + "] is of wrong size, must contain 7 buckets")



        self.assertEqual(3, len(bucket_list_history[it_idx][0]), err_msg + " bucket 0 because of wrong size")

        self.assertTrue(0 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 0")

        self.assertTrue(402 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 402")



        self.assertEqual(4, len(bucket_list_history[it_idx][1]), err_msg + " bucket 1 because of wrong size")

        self.assertTrue(6411 in bucket_list_history[it_idx][1], err_msg + " bucket 0 because of missing element 6411")

        self.assertTrue(614 in bucket_list_history[it_idx][1], err_msg + " bucket 0 because of missing element 614")

        self.assertTrue(1123515 in bucket_list_history[it_idx][1],

                        err_msg + " bucket 0 because of missing element 1123515")

        self.assertTrue(10216 in bucket_list_history[it_idx][1], err_msg + " bucket 0 because of missing element 10216")



        self.assertEqual(3, len(bucket_list_history[it_idx][2]), err_msg + " bucket 2 because of wrong size")

        self.assertTrue(21 in bucket_list_history[it_idx][2], err_msg + " bucket 0 because of missing element 21")

        self.assertTrue(2123 in bucket_list_history[it_idx][2], err_msg + " bucket 0 because of missing element 2123")

        self.assertTrue(21523 in bucket_list_history[it_idx][2], err_msg + " bucket 0 because of missing element 21523")



        self.assertEqual(1, len(bucket_list_history[it_idx][3]), err_msg + " bucket 3 because of wrong size")

        self.assertTrue(33 in bucket_list_history[it_idx][3], err_msg + " bucket 0 because of missing element 33")



        self.assertEqual(1, len(bucket_list_history[it_idx][4]), err_msg + " bucket 4 because of wrong size")

        self.assertTrue(5142 in bucket_list_history[it_idx][4], err_msg + " bucket 0 because of missing element 5142")



        self.assertEqual(0, len(bucket_list_history[it_idx][5]), err_msg + " bucket 5 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][6]), err_msg + " bucket 6 because of wrong size")



    def test_radix_sort_bucket_lists_iteration3(self):

        bucket_list_history = None

        it_idx = 2

        err_msg = "Radix sort of input array " + str(test_array_iteration) + " failed in iteration " + str(

            it_idx + 1) + " on"

        r = RadixSort()

        result = r.sort(test_array_iteration.copy())

        bucket_list_history = r.get_bucket_list_history()



        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")

        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,

                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")



        self.assertEqual(3, len(bucket_list_history[it_idx][0]), err_msg + " bucket 0 because of wrong size")

        self.assertTrue(0 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 0")

        self.assertTrue(21 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 21")

        self.assertTrue(33 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 33")


        #3
        self.assertEqual(2, len(bucket_list_history[it_idx][1]), err_msg + " bucket 1 because of wrong size")

        self.assertTrue(2123 in bucket_list_history[it_idx][1], err_msg + " bucket 0 because of missing element 2123")


        self.assertTrue(5142 in bucket_list_history[it_idx][1],

                        err_msg + " bucket 0 because of missing element 5142")



        self.assertEqual(1, len(bucket_list_history[it_idx][2]), err_msg + " bucket 2 because of wrong size")

        self.assertTrue(10216 in bucket_list_history[it_idx][2], err_msg + " bucket 0 because of missing element 10216")



        self.assertEqual(0, len(bucket_list_history[it_idx][3]), err_msg + " bucket 3 because of wrong size")


        #1
        self.assertEqual(2, len(bucket_list_history[it_idx][4]), err_msg + " bucket 4 because of wrong size")

        self.assertTrue(402 in bucket_list_history[it_idx][4], err_msg + " bucket 0 because of missing element 402")


        #2
        self.assertEqual(3, len(bucket_list_history[it_idx][5]), err_msg + " bucket 5 because of wrong size")

        self.assertTrue(1123515 in bucket_list_history[it_idx][5],

                        err_msg + " bucket 0 because of missing element 1123515")

        self.assertTrue(164504 in bucket_list_history[it_idx][5],

                        err_msg + " bucket 0 because of missing element 164504")


        #0
        self.assertEqual(1, len(bucket_list_history[it_idx][6]), err_msg + " bucket 6 because of wrong size")




    def test_radix_sort_bucket_lists_iteration4(self):

        bucket_list_history = None

        it_idx = 3

        err_msg = "Radix sort of input array " + str(test_array_iteration) + " failed in iteration " + str(

            it_idx + 1) + " on"

        r = RadixSort()

        result = r.sort(test_array_iteration.copy())

        bucket_list_history = r.get_bucket_list_history()



        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")

        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,

                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")



        self.assertEqual(6, len(bucket_list_history[it_idx][0]), err_msg + " bucket 0 because of wrong size")

        self.assertTrue(0 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 0")

        self.assertTrue(21 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 21")

        self.assertTrue(33 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 33")

        self.assertTrue(402 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 402")

        self.assertTrue(614 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 614")



        self.assertEqual(1, len(bucket_list_history[it_idx][1]), err_msg + " bucket 1 because of wrong size")

        self.assertTrue(21523 in bucket_list_history[it_idx][1], err_msg + " bucket 0 because of missing element 21523")



        self.assertEqual(1, len(bucket_list_history[it_idx][2]), err_msg + " bucket 2 because of wrong size")

        self.assertTrue(2123 in bucket_list_history[it_idx][2], err_msg + " bucket 0 because of missing element 2123")



        self.assertEqual(1, len(bucket_list_history[it_idx][3]), err_msg + " bucket 3 because of wrong size")

        self.assertTrue(1123515 in bucket_list_history[it_idx][3],

                        err_msg + " bucket 0 because of missing element 1123515")



        self.assertEqual(1, len(bucket_list_history[it_idx][4]), err_msg + " bucket 4 because of wrong size")

        self.assertTrue(164504 in bucket_list_history[it_idx][4],

                        err_msg + " bucket 0 because of missing element 164504")



        self.assertEqual(1, len(bucket_list_history[it_idx][5]), err_msg + " bucket 5 because of wrong size")

        self.assertTrue(5142 in bucket_list_history[it_idx][5], err_msg + " bucket 0 because of missing element 5142")



        self.assertEqual(1, len(bucket_list_history[it_idx][6]), err_msg + " bucket 6 because of wrong size")

        self.assertTrue(6411 in bucket_list_history[it_idx][6], err_msg + " bucket 0 because of missing element 6411")





    def test_radix_sort_bucket_lists_iteration5(self):

        bucket_list_history = None

        it_idx = 4

        err_msg = "Radix sort of input array " + str(test_array_iteration) + " failed in iteration " + str(

            it_idx + 1) + " on"

        r = RadixSort()

        result = r.sort(test_array_iteration.copy())

        bucket_list_history = r.get_bucket_list_history()



        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")

        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,

                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")



        self.assertEqual(8, len(bucket_list_history[it_idx][0]), err_msg + " bucket 0 because of wrong size")

        self.assertTrue(0 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 0")

        self.assertTrue(21 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 21")

        self.assertTrue(33 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 33")

        self.assertTrue(402 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 402")

        self.assertTrue(614 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 614")

        self.assertTrue(2123 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 2123")

        self.assertTrue(5142 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 5142")

        self.assertTrue(6411 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 6411")



        self.assertEqual(1, len(bucket_list_history[it_idx][1]), err_msg + " bucket 1 because of wrong size")

        self.assertTrue(10216 in bucket_list_history[it_idx][1], err_msg + " bucket 0 because of missing element 10216")



        self.assertEqual(2, len(bucket_list_history[it_idx][2]), err_msg + " bucket 2 because of wrong size")

        self.assertTrue(21523 in bucket_list_history[it_idx][2], err_msg + " bucket 0 because of missing element 21523")

        self.assertTrue(1123515 in bucket_list_history[it_idx][2],

                        err_msg + " bucket 0 because of missing element 1123515")



        self.assertEqual(0, len(bucket_list_history[it_idx][3]), err_msg + " bucket 3 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][4]), err_msg + " bucket 4 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][5]), err_msg + " bucket 5 because of wrong size")



        self.assertEqual(1, len(bucket_list_history[it_idx][6]), err_msg + " bucket 6 because of wrong size")

        self.assertTrue(164504 in bucket_list_history[it_idx][6], err_msg + " bucket 0 because of missing element 6411")



    def test_radix_sort_bucket_lists_iteration6(self):

        bucket_list_history = None

        it_idx = 5

        err_msg = "Radix sort of input array " + str(test_array_iteration) + " failed in iteration " + str(

            it_idx + 1) + " on"

        r = RadixSort()

        result = r.sort(test_array_iteration.copy())

        bucket_list_history = r.get_bucket_list_history()



        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")

        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,

                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")



        self.assertEqual(10, len(bucket_list_history[it_idx][0]), err_msg + " bucket 0 because of wrong size")

        self.assertTrue(0 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 0")

        self.assertTrue(21 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 21")

        self.assertTrue(33 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 33")

        self.assertTrue(402 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 402")

        self.assertTrue(614 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 614")

        self.assertTrue(2123 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 2123")

        self.assertTrue(5142 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 5142")

        self.assertTrue(6411 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 6411")

        self.assertTrue(10216 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 10216")

        self.assertTrue(21523 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 21523")



        self.assertEqual(2, len(bucket_list_history[it_idx][1]), err_msg + " bucket 1 because of wrong size")

        self.assertTrue(1123515 in bucket_list_history[it_idx][1],

                        err_msg + " bucket 0 because of missing element 1123515")

        self.assertTrue(164504 in bucket_list_history[it_idx][1],

                        err_msg + " bucket 0 because of missing element 164504")



        self.assertEqual(0, len(bucket_list_history[it_idx][2]), err_msg + " bucket 2 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][3]), err_msg + " bucket 3 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][4]), err_msg + " bucket 4 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][5]), err_msg + " bucket 5 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][6]), err_msg + " bucket 6 because of wrong size")




    def test_radix_sort_bucket_lists_iteration7(self):

        bucket_list_history = None

        it_idx = 6

        err_msg = "Radix sort of input array " + str(test_array_iteration) + " failed in iteration " + str(

            it_idx + 1) + " on"

        r = RadixSort()

        result = r.sort(test_array_iteration.copy())

        bucket_list_history = r.get_bucket_list_history()



        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")

        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,

                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")



        self.assertEqual(11, len(bucket_list_history[it_idx][0]), err_msg + " bucket 0 because of wrong size")

        self.assertTrue(0 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 0")

        self.assertTrue(21 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 21")

        self.assertTrue(33 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 33")

        self.assertTrue(402 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 402")

        self.assertTrue(614 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 614")

        self.assertTrue(2123 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 2123")

        self.assertTrue(5142 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 5142")

        self.assertTrue(6411 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 6411")

        self.assertTrue(10216 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 10216")

        self.assertTrue(21523 in bucket_list_history[it_idx][0], err_msg + " bucket 0 because of missing element 21523")

        self.assertTrue(164504 in bucket_list_history[it_idx][0],

                        err_msg + " bucket 0 because of missing element 164504")



        self.assertEqual(1, len(bucket_list_history[it_idx][1]), err_msg + " bucket 1 because of wrong size")

        self.assertTrue(1123515 in bucket_list_history[it_idx][1],

                        err_msg + " bucket 0 because of missing element 1123515")



        self.assertEqual(0, len(bucket_list_history[it_idx][2]), err_msg + " bucket 2 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][3]), err_msg + " bucket 3 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][4]), err_msg + " bucket 4 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][5]), err_msg + " bucket 5 because of wrong size")



        self.assertEqual(0, len(bucket_list_history[it_idx][6]), err_msg + " bucket 6 because of wrong size")


    @classmethod

    def tearDownClass(self):

        pass


    ####################################################

    # help methods

    ####################################################



    def list2reason(self, exc_list):

        if exc_list and exc_list[-1][0] is self:

            return exc_list[-1][1]



    def _test_list_forward(self, head=None, tail=None, list=[]):

        current = head


        if (len(list) == 0):

            if (head == None and tail == None):

                return None

            else:

                return "List should be empty - head or tail is not None!"


        elif (len(list) == 1):

            if (head != tail):

                return "Head and tail are not equal in a list with size 1!"

            if (head.get_next() != None):

                return "Next of Head/Tail should be None (listsize == 1)!"

            if (list[0] != head.get_element()):

                return "Wrong element at index 0 (head)! Expected [" + str(list[0]) + "] but found [" + str(

                    head.get_element()) + "]"

            else:

                return None

        # list with size > 1

        for i in range(0, len(list)):

            if (current == head):

                if (current.get_next() == None):

                    return "Next of head is None (listsize > 1)!"

                if (list[i] != current.get_element()):

                    return "Wrong element at index " + str(i) + " (head)! Expected [" + str(

                        list[i]) + "] but found [" + str(current.get_element()) + "]"

                if (list[i + 1] != current.get_next().get_element()):

                    return "Wrong next element of index " + str(i) + " (head)! Expected [" + str(

                        list[i + 1]) + "] but found [" + str(current.get_next().get_element()) + "]"



            elif (current == tail):

                if (list[i] != current.get_element()):

                    return "Wrong element at index " + str(i) + " (tail)! Expected [" + str(

                        list[i]) + "] but found [" + str(current.get_element()) + "]"

                if (current.get_next() != None):

                    return "Next of tail is not None!"



            else:

                if (list[i] != current.get_element()):

                    return "Wrong element at index " + str(i) + "! Expected [" + str(

                        list[i]) + "] but found [" + str(current.get_element()) + "]"

                if current.get_next() == None:

                    if i != len(list) - 1:

                        return "Wrong next element of index " + str(i) + "! Expected [" + str(

                            list[i + 1]) + "] but found None"

                    else:

                        return None

                elif (list[i + 1] != current.get_next().get_element()):

                    return "Wrong next element of index " + str(i) + "! Expected [" + str(

                        list[i + 1]) + "] but found [" + str(current.get_next().get_element()) + "]"



            current = current.get_next()



        return None





if __name__ == "__main__":

    unittest.main()
