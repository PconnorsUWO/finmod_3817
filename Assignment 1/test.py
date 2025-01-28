import numpy as np
import sympy as sp
from scipy.optimize import differential_evolution
functions = [
    "x**4 + x**2 - 6*x*y + 3*y**2",
    "x**2 - 6*x*y + 2*y**2 + 10*x + 2*y - 5",
    "x*y**2 + x**3*y - x*y",
    "3*x**4 + 3*x**2*y - y**3",
]

results = []

for func_str in functions:
    func = sp.sympify(func_str)
    x, y = sp.symbols('x y')
    scipy_func = sp.lambdify((x, y), func, 'numpy')

    def f(xy):
        return scipy_func(xy[0], xy[1])

    def neg_f(xy):
        return -f(xy)

    bounds = [(-10, 10), (-10, 10)]

    max_result = differential_evolution(neg_f, bounds)
    min_result = differential_evolution(f, bounds)

    global_maximum = -max_result.fun
    max_location = max_result.x
    global_minimum = min_result.fun
    min_location = min_result.x

    results.append((global_maximum, max_location, global_minimum, min_location))

for i, res in enumerate(results):
    print(f"Function {chr(97 + i)}")
    print(f"Global Maximum: {res[0]} at {res[1]}")
    print(f"Global Minimum: {res[2]} at {res[3]}")

