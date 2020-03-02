import unittest

def fun(x):
    print (x + 1)

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
