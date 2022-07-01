
class RadixSort:
    def __init__(self):
        self.base = 7
        #                                _________list of bucketlists
        #                               | ________list of buckets -> list of buckets as array here
        #                               || ___________content of a bucket -> buckets as arrays here
        #                               |||
        self.bucket_list_history = []  #[[[]]] -> will look like this in the end

    def get_bucket_list_history(self):
        return self.bucket_list_history

    def sort(self, list):
        """
        Sorts a given list using radixsort in descending order
        @param list to be sorted
        @returns the sorted list as an 1D array
        @raises ValueError if the list is None
        """
        self.bucket_list_history.clear()    #clear history list at beginning of sorting

        if list is None:
            return ValueError

        """# Step 1 -> Find the maximum element in the input array, and number of digits in the `max` element
            maxEl = max(inputArray)
            D = 1
            while maxEl > 0:
                maxEl /= 10
                D += 1"""

        # Step 1 Find max element in input array, and its number of digits
        max_digit = len(str(max(list)))

        # Step 3 -> Initialize the place value to the least significant place
        placeVal = 1

        # Step 4
        outputArray = list
        while max_digit > 0:
            outputArray = self.countingSortForRadix(outputArray, placeVal)
            print(outputArray)
            #self._add_bucket_list_to_history(outputArray)
            placeVal *= 10
            max_digit -= 1

        return outputArray


    def countingSortForRadix(self, inputArray, placeValue):
        # We can assume that the number of digits used to represent
        # all numbers on the placeValue position is not grater than 10
        base = 7  # elements from 0 to 6
        countArray = [0] * base  # creating bucket list for all 7 possible numbers
        inputSize = len(inputArray)

        # placeElement is the value of the current place value
        # of the current element, e.g. if the current element is
        # 123, and the place value is 10, the placeElement is
        # equal to 2
        for i in range(inputSize):
            placeElement = (inputArray[i] // placeValue) % 10
            countArray[placeElement] += 1

        # cumulative count for ascending
        #for i in range(1, base):
        #    countArray[i] += countArray[i-1]

        #for descending
        for i in range(base - 2, -1, -1):
            countArray[i] += countArray[i + 1]

        # Reconstructing the output array
        outputArray = [0] * inputSize  # output array same size as input array
        i = inputSize - 1  # starting from back (last element)
        while i >= 0:
            currentEl = inputArray[i]  # looking at last element of input array
            placeElement = (inputArray[
                                i] // placeValue) % 10  # looking at the corresponding placeValue (Decimalstelle)
            countArray[placeElement] -= 1               # decrease the cumulative counter for this element
            newPosition = countArray[placeElement]      # index of this element in the sorted array
            outputArray[newPosition] = currentEl        # put element in right position at sorted array
            i -= 1                                      # decrease counter for next element in input array

        return outputArray

    def sort2(self, list):
        """
        Sorts a given list using radixsort in ascending order
        @param list to be sorted
        @returns the sorted list as an 1D array
        @raises ValueError if the list is None
        """
        self.bucket_list_history.clear()  # clear history list at beginning of sorting

        if list is None:
            raise ValueError
        max_key_length = 0
        # getting the length of largest key to be able to use it to define iteration passes
        for item in list:
            length = len(str(item))
            if length > max_key_length:
                max_key_length = length

        for i in range(max_key_length):
            bucket_list = [[] for _ in range(self.base)]
            print(list)
            for key in list:
                i_digit = (key // 10 ** i) % 10
                # formula for extracting ith digit of key k. using m= 10 doesn't affect implementation. since we
                # get keys as decimal already in base 7, we can use m = 10 here.
                if i_digit == 0:
                    bucket_list[len(bucket_list) - 1].append(key)
                else:
                    bucket_list[(-i_digit) - 1].append(key)
                # bucket_list[i_digit].append(key)
            #self._add_bucket_list_to_history(bucket_list)

            count = 0
            for bucket in bucket_list:
                for k in bucket:
                    list[count] = k
                    count += 1

        return list


    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucketlist and adds it to the bucketlistHistory.
        @param bucket_list is your current bucketlist, after assigning all elements to be sorted to the buckets.
        """
        arr_clone = []
        for i in range(0, len(bucket_list)):
            arr_clone.append([])
            for j in bucket_list[i]:
                arr_clone[i].append(j)

        self.bucket_list_history.append(arr_clone)

        """ 
        #returns the digit (base7) of val at position pos 
        def get_digit(val, pos)
        
        # calculates buckets for position pos 
        def bucketSort(pos, buckets)
        
        # Merges bucket lists into one list 
        def merge(buckets)
        
        Time Complexity:
        The time complexity of radix sort is Θ((N+b)*logb(max)) in all cases, where:

        N is the number of elements in unsorted array.
        b is the base of input array, for example, for decimal system, b is 10.
        max is the maximum element of the input array."""
