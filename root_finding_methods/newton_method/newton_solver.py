import math
from typing import Callable, Tuple

class NewtonMethodSolver:
    def __init__(self,
                 max_iterations: int = 100,
                 tolerance: float = 1e-6,
                 divergence_threshold: float = 1e10):
        """
        Initialize Newton's method solver with divergence detection.

        Args:
            max_iterations (int): Maximum iteration limit
            tolerance (float): Convergence threshold
            divergence_threshold (float): Maximum value before considering divergence

        Raises:
            ValueError: If parameters are invalid
        """
        if max_iterations <= 0:
            raise ValueError("Max iterations must be positive")
        if tolerance <= 0:
            raise ValueError("Tolerance must be positive")

        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.divergence_threshold = divergence_threshold

    def check_derivative(self, func: Callable[[float], float], deriv: Callable[[float], float], x: float) -> bool:
        epsilon = 1e-7  # Small perturbation for numerical derivative
        numerical_deriv = (func(x + epsilon) - func(x)) / epsilon  # Numerical approximation of the derivative
        provided_deriv = deriv(x)

        # Print for debugging
        print(f"At x = {x}:")
        print(f"Numerical Derivative: {numerical_deriv}")
        print(f"Provided Derivative: {provided_deriv}")
        print(f"Difference: {abs(numerical_deriv - provided_deriv)}")
        print("-" * 20)

        # Check if the absolute difference is within the tolerance
        return abs(numerical_deriv - provided_deriv) < self.tolerance


    def solve(self,
              func: Callable[[float], float],
              deriv: Callable[[float], float],
              initial_guess: float) -> Tuple[float, int]:
        """
        Find root using Newton's method with divergence detection.
        """
        # Input validation
        if not (callable(func) and callable(deriv)):
            raise TypeError("Function and derivative must be callable")

        # Check if the provided derivative is correct
        if not self.check_derivative(func, deriv, initial_guess):
            raise ValueError("The provided derivative is not the correct derivative of the function")

        x = initial_guess
        for iterations in range(self.max_iterations):
            fx = func(x)

            # Check convergence
            if abs(fx) < self.tolerance:
                return x, iterations

            # Check divergence
            if abs(x) > self.divergence_threshold:
                raise ValueError(f"Solution diverged after {iterations} iterations")

            # Compute derivative
            dfx = deriv(x)

            # Prevent division by zero
            if abs(dfx) < self.tolerance:
                raise ValueError("Derivative too close to zero")

            # Newton's method update
            x = x - fx / dfx

        raise ValueError(f"Failed to converge after {self.max_iterations} iterations")
