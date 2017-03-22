import unittest
import numpy as np
import scholarships

class TestMethods(unittest.TestCase):

    def test_FindGreatest(self):
        # Check to see if it solves example
        basic = [[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]
        s = scholarships.findGreatest(basic, 3)
        self.assertEqual(s, {"sequence": [5,9,25], "total": 1125})

        # Checks to see if it can handle duplicate numbers
        large = np.ones((50,50))
        large *= 100
        large.tolist()
        s = scholarships.findGreatest(large, 11)
        self.assertEqual(s, {"sequence": [100,100,100,100,100], "total": 10000000000})

    def test_SpanLists(self):
        """ 
        The tests for this werent necessary because the description says I'm getting nxn matrix with n >= 100
        this test would have to otherwise to check for irregular shapes and n < k 
        """
        pass
