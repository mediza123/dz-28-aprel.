import unittest
import sys

def factorial(num: int):
    if num < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if num == 0:
        return 1
    res = 1
    for j in range(1, num + 1):
        res *= j
        if res > sys.maxsize:
            raise ValueError(f"Факториал для {num} не поддерживается типом int")
    return res

class TestFactorial(unittest.TestCase):
    def test_zero_case(self):
        self.assertEqual(factorial(0), 1)
    
    def test_unit_case(self):
        self.assertEqual(factorial(1), 1)
    
    def test_positive_values(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
    
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            factorial(-3)
    
    def test_overflow_case(self):
        with self.assertRaises(ValueError):
            factorial(1000)
    
    def test_boundary_condition(self):
        max_val = 1
        k = 1
        while True:
            try:
                max_val = factorial(k)
                k += 1
            except ValueError:
                break
        self.assertGreater(k, 1)

if __name__ == '__main__':
    unittest.main()
