import unittest

def check(x):

    return x >= 100

class MyCheck(unittest.TestCase):

        def test(self):
            self.assertTrue(check(100),True)

if __name__== '__main__':
