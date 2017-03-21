import unittest
import scholarships

class TestMethods(unittest.TestCase):

    def test_FindGreatest(self):
        basic = [[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]
        s = scholarships.findGreatest(basic, 3)
        self.assertEqual(s, {"sequence": [5,9,25], "total": 1125})

    def test_SpanLists(self):
        pass
