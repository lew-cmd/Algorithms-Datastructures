import unittest

from datetime import date
from RabinKarp import RabinKarp


class TestAssignment07RabinKarp(unittest.TestCase):

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


    ###############################################
    ################## Test cases##################
    ###############################################

    def test_is_empty(self):
        r=RabinKarp()
        try:
            r.search("aaa", "")
        except ValueError:
            self.assertTrue("ValueError should be raised when looking for a pattern in an empty string")


    def test_kmp_special1(self):
        r=RabinKarp()
        res=r.search("xxx", "xxxxflkaxxxxA")
        print(res)
        print("\n")

        self.assertTrue(len(res) > 0)
        self.assertEqual(4, len(res), "expected 4 elements")

        targets=[0,1,8,9]
        indices=res
        indices.sort()

        res_correct=True
        target_to_find=0
        for i in range(0, len(indices)):
            if target_to_find >= len(targets):
                res_correct=False
            elif indices[i] == targets[target_to_find]:
                target_to_find+=1

        if target_to_find < len(targets):
            res_correct=False

        self.assertTrue(res_correct)

    def test_kmp_special2(self):
        r=RabinKarp()
        res=r.search("xyxy", "xxyxyxyflkaxyxxyxyA")
        print(res)
        print("\n")

        self.assertTrue(len(res) > 0)
        self.assertEqual(3, len(res), "expected 3 elements")

        targets=[1,3,14]
        indices=res
        indices.sort()

        res_correct=True
        target_to_find=0
        for i in range(0, len(indices)):
            if target_to_find >= len(targets):
                res_correct=False
            elif indices[i] == targets[target_to_find]:
                target_to_find+=1

        if target_to_find < len(targets):
            res_correct=False

        self.assertTrue(res_correct)



    def test_kmp_short(self):
        r = RabinKarp()
        res = r.search("xxx", "abcdexxxunbxxxxke")
        print(res)
        print("\n")

        self.assertTrue(len(res) > 0)
        self.assertEqual(3, len(res), "expected 3 elements")

        targets = [5, 11, 12]
        indices = res
        indices.sort()

        res_correct = True
        target_to_find = 0
        for i in range(0, len(indices)):
            if target_to_find >= len(targets):
                res_correct = False
            elif indices[i] == targets[target_to_find]:
                target_to_find += 1

        if target_to_find < len(targets):
            res_correct = False

        self.assertTrue(res_correct)

    def test_kmp_long(self):
        r = RabinKarp()
        res = r.search("is","Compares two strings lexicographically. The comparison is based on the Unicode value of each character in the strings. The character sequence represented by this String object is compared lexicographically to the character sequence represented by the argument string. The result is a negative integer if this String object lexicographically precedes the argument string. The result is a positive integer if this String object lexicographically follows the argument string. The result is zero if the strings are equal; compareTo returns 0 exactly when the equals(Object) method would return true.")


        print(res)
        print("\n")

        self.assertTrue(len(res) > 0)
        self.assertEqual(9, len(res), "expected 9 elements")

        targets = [50, 55, 159, 176, 279, 306, 382, 409, 484]
        indices = res
        indices.sort()

        res_correct = True
        target_to_find = 0
        for i in range(0, len(indices)):
            if target_to_find >= len(targets):
                res_correct = False
            elif indices[i] == targets[target_to_find]:
                target_to_find += 1

        if target_to_find < len(targets):
            res_correct = False

        self.assertTrue(res_correct)

    def test_kmp_long_pattern(self):
        r = RabinKarp()
        res = r.search("ijK lmnopq","abcdefghijK lmnopqrstuvwxyz, abcdefghijK lmnopqrstuvwxyz.ijk lmnopqr")


        print(res)
        print("\n")

        self.assertTrue(len(res) > 0)
        self.assertEqual(2, len(res), "expected 2 elements")

        targets = [8,37]
        indices = res
        indices.sort()

        res_correct = True
        target_to_find = 0
        for i in range(0, len(indices)):
            if target_to_find >= len(targets):
                res_correct = False
            elif indices[i] == targets[target_to_find]:
                target_to_find += 1

        if target_to_find < len(targets):
            res_correct = False

        self.assertTrue(res_correct)


    def test_kmp_special(self):
        r = RabinKarp()
        res = r.search("xxx", "xxxxxA")
        print(res)
        print("\n")

        self.assertTrue(len(res) > 0)
        self.assertEqual(3, len(res), "expected 3 elements")

        targets = [0, 1, 2]
        indices = res
        indices.sort()

        res_correct = True
        target_to_find = 0
        for i in range(0, len(indices)):
            if target_to_find >= len(targets):
                res_correct = False
            elif indices[i] == targets[target_to_find]:
                target_to_find += 1

        if target_to_find < len(targets):
            res_correct = False

        self.assertTrue(res_correct)

    def test_rabin_karp_hash_of_pattern(self):
        r = RabinKarp()
        str_pattern = "ef"
        hash_pattern = r.get_rolling_hash_value(str_pattern, '\0', 0)
        self.assertEqual(3031, hash_pattern)

    def test_rabin_karp_hash_of_text_sequences(self):
        r = RabinKarp()

        str_text = "abcdef"
        hash = 0

        hash = r.get_rolling_hash_value(str_text[0:2], '\0', hash)
        self.assertEqual(2911, hash, "Wrong hash value. Initial text: abcdef")

        hash = r.get_rolling_hash_value(str_text[1:3], 'a', hash)
        self.assertEqual(2941, hash, "Wrong hash value. Initial text: abcdef")

        hash = r.get_rolling_hash_value(str_text[2:4], 'b', hash)
        self.assertEqual(2971, hash, "Wrong hash value. Initial text: abcdef")

        hash = r.get_rolling_hash_value(str_text[3:5], 'c', hash)
        self.assertEqual(3001, hash, "Wrong hash value. Initial text: abcdef")

        hash = r.get_rolling_hash_value(str_text[4:6], 'd', hash)
        self.assertEqual(3031, hash, "Wrong hash value. Initial text: abcdef")


    def test_kmp_very_long_pattern(self):
        r = RabinKarp()
        res = r.search("Lorem ips","Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod "
				+ "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo "
				+ "dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum "
				+ "dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam "
				+ "erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea "
				+ "takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam "
				+ "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et "
				+ "justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. "
				+ "Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat "
				+ "nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue "
				+ "duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy "
				+ "nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud "
				+ "exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor "
				+ "in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et "
				+ "accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla "
				+ "facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer "
				+ "possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut "
				+ "laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper "
				+ "suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate "
				+ "velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis. At vero eos et accusam et justo duo dolores "
				+ "et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit "
				+ "amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed "
				+ "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "
				+ "sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam aliquyam "
				+ "diam diam dolore dolores duo eirmod eos erat, et nonumy sed tempor et et invidunt justo labore Stet clita ea et "
				+ "gubergren, kasd magna no rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor sit amet. Lorem ipsum "
				+ "dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam "
				+ "erat. Consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed "
				+ "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "
				+ "sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod "
				+ "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores "
				+ "et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit "
				+ "amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed "
				+ "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "
				+ "sanctus. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et "
				+ "dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita "
				+ "kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur "
				+ "sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. "
				+ "At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem "
				+ "ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt "
				+ "ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "
				+ "Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in"
				+ " hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et "
				+ "accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla "
				+ "facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut "
				+ "laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper "
				+ "suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate "
				+ "velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio "
				+ "dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor "
				+ "cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum "
				+ "dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam "
				+ "erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip "
				+ "ex ea commodo "
				+ "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod "
				+ "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo "
				+ "dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum "
				+ "dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam "
				+ "erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea "
				+ "takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam "
				+ "nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et "
				+ "justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. "
				+ "Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat "
				+ "nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue "
				+ "duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy "
				+ "nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud "
				+ "exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor "
				+ "in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et "
				+ "accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla "
				+ "facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer "
				+ "possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut "
				+ "laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper "
				+ "suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate "
				+ "velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis. At vero eos et accusam et justo duo dolores "
				+ "et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit "
				+ "amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed "
				+ "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "
				+ "sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam aliquyam "
				+ "diam diam dolore dolores duo eirmod eos erat, et nonumy sed tempor et et invidunt justo labore Stet clita ea et "
				+ "gubergren, kasd magna no rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor sit amet. Lorem ipsum "
				+ "dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam "
				+ "erat. Consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed "
				+ "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "
				+ "sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod "
				+ "tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores "
				+ "et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit "
				+ "amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed "
				+ "diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata "
				+ "sanctus. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et "
				+ "dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita "
				+ "kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur "
				+ "sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. "
				+ "At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem "
				+ "ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt "
				+ "ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "
				+ "Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in"
				+ " hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et "
				+ "accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla "
				+ "facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut "
				+ "laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper "
				+ "suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate "
				+ "velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio "
				+ "dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor "
				+ "cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum "
				+ "dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam "
				+ "erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip "
				+ "ex ea commodo.")

        print(res)
        print("\n")

        self.assertTrue(len(res) > 0)
        self.assertEqual(52, len(res), "expected 52 elements")

        targets=[0, 268, 296, 564, 592, 860, 1159, 1826, 2345, 2373, 2641, 2669, 2937, 2965, 3342, 3370, 3638, 3666,
                     3931, 4199, 4227, 4495, 4523, 4791, 5090, 5757, 6019, 6287, 6315, 6583, 6611, 6879, 7178, 7845,
                     8364, 8392, 8660, 8688, 8956, 8984, 9361, 9389, 9657, 9685, 9950, 10218, 10246, 10514, 10542,
                     10810, 11109, 11776]

        indices = res
        indices.sort()

        res_correct = True
        target_to_find = 0
        for i in range(0, len(indices)):
            if target_to_find >= len(targets):
                res_correct = False
            elif indices[i] == targets[target_to_find]:
                target_to_find += 1

        if target_to_find < len(targets):
            res_correct = False

        self.assertTrue(res_correct)

    ####################################################
    # help methods
    ####################################################

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]


def check_search_result_empty(test, str_pattern, str_text):
    err_msg = "RabinKarp.search() with input pattern \"" + str_pattern + "\" and input text \"" + str_text + "\""
    result = None

    try:
        result = RabinKarp().search(str_pattern, str_text)
    except Exception as ex:
        test.fail(err_msg + "raised an exception: " + repr(ex))

    test.assertIsNotNone(result, msg=err_msg + "should not return a class result which is null!")
    test.assertEqual(len(result.result_indices), 0, msg=err_msg + ": Pattern should not be found but found " + str(
        result.count) + " time(s) at idx " + ' '.join(map(str, result.result_indices)) + ".")
    test.assertEqual(result.count, 0, msg=err_msg + ": Pattern should not be found but found " + str(
        result.count) + " time(s) at idx " + ' '.join(map(str, result.result_indices)) + ".")


def check_search_result(test, str_pattern, str_text, expected_result):
    err_msg = "RabinKarp.search() with input pattern \"" + str_pattern + "\" and input text \"" + str_text + "\""
    result = None

    try:
        result = RabinKarp().search(str_pattern, str_text)
    except Exception as ex:
        test.fail(err_msg + "raised an exception: " + repr(ex))

    test.assertIsNotNone(result, msg=err_msg + "should not return a class result which is null!")
    test.assertEqual(result.count, len(expected_result),
                     msg=err_msg + "returned wrong result.count: " + str(result.count))

    indices = result.result_indices
    indices.sort()

    test.assertListEqual(expected_result, indices)


if __name__ == '__main__':
    unittest.main()
