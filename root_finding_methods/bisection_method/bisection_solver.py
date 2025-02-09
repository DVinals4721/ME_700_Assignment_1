import math
from typing import Callable, Optional, Tuple

class BisectionSolver:
    def __init__(self, max_iterations: int = 100, tolerance: float = 1e-6):
        if max_iterations <= 0:
            raise ValueError("Max iterations must be a positive integer")
        if tolerance <= 0:
            raise ValueError("Tolerance must be a positive float")

        self.max_iterations = max_iterations
        self.tolerance = tolerance

    def solve(self, func: Callable[[float], float], a: float, b: float) -> Tuple[float, int]:
        if not callable(func):
            raise TypeError("Input must be a callable function")

        fa = func(a)
        fb = func(b)

        # If one of the endpoints is a root, return it
        if abs(fa) < self.tolerance:
            return a, 0
        if abs(fb) < self.tolerance:
            return b, 0

        # If the function has the same sign at both endpoints, try to find a bracket
        if fa * fb > 0:
            c = self._find_bracket(func, a, b)
            if c is None:
                raise ValueError(f"Root cannot be bracketed: f({a})={fa}, f({b})={fb}")
            if abs(a - c) < abs(b - c):
                a, fa = c, func(c)
            else:
                b, fb = c, func(c)

        # Ensure a < b
        if a > b:
            a, b = b, a
            fa, fb = fb, fa

        # Bisection method
        iterations = 0
        while iterations < self.max_iterations:
            c = (a + b) / 2
            fc = func(c)

            if abs(fc) < self.tolerance or (b - a) / 2 < self.tolerance:
                return c, iterations

            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

            iterations += 1

        # If max iterations reached, return the best approximation
        return (a + b) / 2, iterations

    def _find_bracket(self, func: Callable[[float], float], a: float, b: float) -> Optional[float]:
        """Attempt to find a point c where func(c) has opposite sign of func(a) and func(b)"""
        fa, fb = func(a), func(b)
        for _ in range(50):  # Limit the number of attempts
            c = (a + b) / 2
            fc = func(c)
            if fc * fa < 0 or fc * fb < 0:
                return c
            if abs(fc) < abs(fa):
                a, fa = c, fc
            else:
                b, fb = c, fc
        return None