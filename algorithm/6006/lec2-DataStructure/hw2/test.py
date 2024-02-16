import unittest
from recitation2 import Array_seq, Dynamic_Array_Sequence

class TestStaticArr(unittest.TestCase):
    def test_static_array_build_1(self):
        data = [1,2,3,4,5]
        arr = Array_seq()
        arr.build(data)
        res = [x for x in arr.__iter__()]
        self.assertListEqual(data,res)

    def test_static_array_build_2(self):
        data = []
        arr = Array_seq()
        arr.build(data)
        res = [x for x in arr.__iter__()]
        self.assertListEqual(data,res)

    def test_insert_at(self):
        data = [1,2,3,4,5]
        arr = Array_seq()
        arr.build(data)
        arr.insert_at(3,10)
        exp = [1,2,3,10,4,5]
        res = [x for x in arr.__iter__()]
        self.assertListEqual(exp,res)

class TestDynamicArr(unittest.TestCase):
    def test_build(self):
        data = [10,9,8,7]
        tail = [None]*4
        dyna_arr = Dynamic_Array_Sequence()
        dyna_arr.build(data)
        self.assertListEqual(dyna_arr.A,data+tail)




if __name__=="__main__":
    unittest.main()
