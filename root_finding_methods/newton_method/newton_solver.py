import math
from typing import Callable, Tuple

class NewtonMethodSolver:
    def __init__(self,
                 max_iterations: int = 100,
                 tolerance: float = 1e-6,
                 divergence_threshold: float = 1e10,
                 h: float = 1e-7):
        """
        Initialize Newton's method solver with divergence detection and numerical differentiation.

        Args:
            max_iterations (int): Maximum iteration limit
            tolerance (float): Convergence threshold
            divergence_threshold (float): Maximum value before considering divergence
            h (float): Step size for numerical differentiation

        Raises:
            ValueError: If parameters are invalid
        """
        if max_iterations <= 0:
            raise ValueError("Max iterations must be positive")
        if tolerance <= 0:
            raise ValueError("Tolerance must be positive")
        if h <= 0:
            raise ValueError("Step size h must be positive")

        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.divergence_threshold = divergence_threshold
        self.h = h

    def numerical_derivative(self, func: Callable[[float], float], x: float) -> float:
        """
        Calculate the numerical derivative of the function at point x.

        Args:
            func (Callable[[float], float]): The function to differentiate
            x (float): The point at which to calculate the derivative

        Returns:
            float: The numerical derivative
        """
        return (func(x + self.h) - func(x - self.h)) / (2 * self.h)

    def solve(self,
              func: Callable[[float], float],
              initial_guess: float) -> Tuple[float, int]:
        """
        Find root using Newton's method with divergence detection and numerical differentiation.

        Args:
            func (Callable[[float], float]): The function to find the root of
            initial_guess (float): The initial guess for the root

        Returns:
            Tuple[float, int]: The root and the number of iterations

        Raises:
            TypeError: If the function is not callable
            ValueError: If the solution diverges or fails to converge
        """
        if not callable(func):
            raise TypeError("Function must be callable")

        x = initial_guess
        for iterations in range(self.max_iterations):
            fx = func(x)

            # Check convergence
            if abs(fx) < self.tolerance:
                return x, iterations

            # Check divergence
            if abs(x) > self.divergence_threshold:
                raise ValueError(f"Solution diverged after {iterations} iterations")

            # Compute derivative numerically
            dfx = self.numerical_derivative(func, x)

            # Prevent division by zero
            if abs(dfx) < self.tolerance:
                raise ValueError("Derivative too close to zero")

            # Newton's method update
            x = x - fx / dfx

        raise ValueError(f"Failed to converge after {self.max_iterations} iterations")