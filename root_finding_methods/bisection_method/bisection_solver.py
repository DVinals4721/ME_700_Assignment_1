import math
from typing import Callable, Optional, Tuple

class BisectionSolver:
    """
    A robust solver for finding roots of mathematical functions using the bisection method.

    The bisection method is a root-finding algorithm that repeatedly divides an interval-
    in half to narrow down the location of a root (zero) of a continuous function.

    Attributes:
        max_iterations (int): Maximum number of iterations to prevent infinite loops
        tolerance (float): Convergence tolerance for root approximation
    """

    def __init__(self,
                 max_iterations: int = 100,
                 tolerance: float = 1e-6):
        """
        Initialize the BisectionSolver with configuration parameters.

        Args:
            max_iterations (int, optional): Maximum iterations to prevent infinite loops. Defaults to 100.
            tolerance (float, optional): Convergence tolerance for root approximation. Defaults to 1e-6.

        Raises:
            ValueError: If max_iterations is not positive or tolerance is not positive
        """
        if max_iterations <= 0:
            raise ValueError("Max iterations must be a positive integer")
        if tolerance <= 0:
            raise ValueError("Tolerance must be a positive float")

        self.max_iterations = max_iterations
        self.tolerance = tolerance

    def solve(self,
              func: Callable[[float], float],
              a: float,
              b: float) -> Tuple[float, int]:
        """
        Find the root of a function using the bisection method.

        Args:
            func (Callable[[float], float]): Continuous function to find root for
            a (float): Left boundary of initial interval
            b (float): Right boundary of initial interval

        Returns:
            Tuple[float, int]: Approximated root and number of iterations used

        Raises:
            ValueError: If the root cannot be bracketed or no convergence occurs
            TypeError: If input is not a callable function
        """
        # Validate inputs
        if not callable(func):
            raise TypeError("Input must be a callable function")

        # Check if root can be bracketed
        fa = func(a)
        fb = func(b)

        if fa * fb >= 0:
            raise ValueError(f"Root cannot be bracketed: f({a})={fa}, f({b})={fb}")

        # Ensure a < b
        if a > b:
            a, b = b, a
            fa, fb = fb, fa

        # Bisection method
        iterations = 0
        while iterations < self.max_iterations:
            # Calculate midpoint
            c = (a + b) / 2
            fc = func(c)

            # Check convergence
            if abs(fc) < self.tolerance or (b - a) / 2 < self.tolerance:
                return c, iterations

            # Update interval
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

            iterations += 1

        # Raise error if max iterations reached
        raise ValueError(f"Root not found within {self.max_iterations} iterations")


    