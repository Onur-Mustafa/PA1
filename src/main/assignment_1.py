# Import necessary libraries
import math

def approximation_algorithm(x0=1.5, tol=0.000001):
    iter = 0
    x = x0
    diff = x0

    print(f"{iter} : {x}")

    while diff >= tol:
        iter += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"{iter} : {x}")
        diff = abs(x - y)

    print(f"\nConvergence after {iter} iterations")

def bisection_method(f, a, b, tol, max_iter=100):
    left = a
    right = b
    i = 0

    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2

        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p

    return p

def fixed_point_iteration(g, x0, tol, max_iter=100):
    i = 1
    p0 = x0

    while i <= max_iter:
        p = g(p0)
        if abs(p - p0) < tol:
            print(f"p: {p}, SUCCESS")
            return p
        i += 1
        p0 = p

    print("FAILURE")
    return None

def newton_raphson_method(f, df, x0, tol, max_iter=100):
    i = 1
    p_prev = x0

    while i <= max_iter:
        if df(p_prev) != 0:
            p_next = p_prev - f(p_prev) / df(p_prev)
            if abs(p_next - p_prev) < tol:
                print(f"p_next: {p_next}, SUCCESS")
                return p_next
            i += 1
            p_prev = p_next
        else:
            print("Unsuccessful: Derivative is zero")
            return None

    print("Unsuccessful: Max iterations performed")
    return None

if __name__ == "__main__":
    # Example function and its derivative
    def f(x):
        return x**2 - 2

    def df(x):
        return 2*x

    # Example usage of the bisection method
    root = bisection_method(f, 1, 2, 0.000001)
    print(f"Root: {root}")

    # Example function for fixed-point iteration
    def g(x):
        return (x + 2/x) / 2

    # Example usage of the fixed-point iteration
    result = fixed_point_iteration(g, 1.5, 0.000001)
    print(f"Result: {result}")

    # Example usage of the Newton-Raphson method
    root = newton_raphson_method(f, df, 1.5, 0.000001)
    print(f"Root: {root}")

    # Example usage of the algorithms
    approximation_algorithm() 