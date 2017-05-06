import unittest
def first(a,b,c):
    x = (a+b*c)**2
    return  x
def second(a,b,c):
    x =  a - 4 * b // c
    return x
def third(a,b,c):
    x = (a * b + 4) // (c - 1)
    return x
class CheckResult(unittest.TestCase):
    def test_first_result(self):
        result = first(a,b,c)
        self.assertEqual(result,841)
    def test_second_result(self):
        result = second(a,b,c)
        self.assertEqual(result,-5)
    def test_third_result(self):
        result = third(a,b,c)
        self.assertEqual(result,22)
if __name__ =='__main__':
    a = 5
    b = 8
    c = 3
    print(first(a,b,c))
    print(second(a,b,c))
    print(third(a,b,c))
    unittest.main()

