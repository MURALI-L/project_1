import unittest
from calci import Calc
class Testcalc(unittest.TestCase):
    def test_add_valid01(self):
        c=Calc()
        arg1=10
        arg2=20
        expected=30
        actual=c.add(arg1,arg2)
        self.assertEqual(expected,actual,"Test is failed:test_add_valid01")
    def test_add_valid02(self):
        c=Calc()
        arg1=0
        arg2=20
        expected=20
        actual=c.add(arg1,arg2)
        self.assertEqual(expected,actual,"Test is failed:test_add_valid02")
    def test_add_valid03(self):
        c=Calc()
        arg1=-10
        arg2=20
        expected=10
        actual=c.add(arg1,arg2)
        self.assertEqual(expected,actual,"Test is failed:test_add_valid03")
    def test_mul_valid01(self):
        c=Calc()
        arg1=1
        arg2=2
        expected=2
        actual=c.mul(arg1,arg2)
        self.assertEqual(expected,actual,"Test is failed:test_add_valid01")
    def test_mul_valid02(self):
        c=Calc()
        arg1=0
        arg2=20
        expected=0
        actual=c.mul(arg1,arg2)
        self.assertEqual(expected,actual,"Test is failed:test_add_valid02")
    def test_mul_valid03(self):
        c=Calc()
        arg1=10
        arg2=20
        expected=200
        actual=c.mul(arg1,arg2)
        self.assertEqual(expected,actual,"Test is failed:test_add_valid03")
unittest.main()
