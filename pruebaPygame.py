import unittest

def factorial(numero: int):
    if numero in (0, 1):
        return 1
    return numero * factorial(numero - 1)

class TestFactorial(unittest.TestCase):

    def test_1(self):
        self.assertEqual(factorial(4), 24)

if __name__ == '__main__':
    unittest.main()