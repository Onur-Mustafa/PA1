import unittest
from src.main.assignment_1 import (
    approximation_algorithm,
    bisection_method,
    fixed_point_iteration,
    newton_raphson_method
)

class TestAssignment1(unittest.TestCase):
    def test_approximation_algorithm(self):
        
        pass

    def test_bisection_method(self):
        def f(x):
            return x**2 - 2
        root = bisection_method(f, 1, 2, 0.000001)
        self.assertAlmostEqual(root, 1.414213, places=5)

    def test_fixed_point_iteration(self):
        def g(x):
            return (x + 2/x) / 2
        result = fixed_point_iteration(g, 1.5, 0.000001)
        self.assertAlmostEqual(result, 1.414213, places=5)

    def test_newton_raphson_method(self):
        def f(x):
            return x**2 - 2
        def df(x):
            return 2*x
        root = newton_raphson_method(f, df, 1.5, 0.000001)
        self.assertAlmostEqual(root, 1.414213, places=5)

if __name__ == '__main__':
    unittest.main() 