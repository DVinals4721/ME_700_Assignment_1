import math
import numpy as np
from typing import Callable, Tuple

class NewtonMethodSolver:
    def __init__(self,
                 max_iterations: int = 100,
                 tolerance: float = 1e-6,
                 divergence_threshold: float = 1e10,
                 h: float = 1e-7):
        """
        Initialize Newton's method solver for systems of equations with divergence detection and numerical differentiation.

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

    def numerical_jacobian(self, func: Callable[[np.ndarray], np.ndarray], x: np.ndarray) -> np.ndarray:
        """
        Calculate the numerical Jacobian of the function at point x.

        Args:
            func (Callable[[np.ndarray], np.ndarray]): The system of equations
            x (np.ndarray): The point at which to calculate the Jacobian

        Returns:
            np.ndarray: The numerical Jacobian
        """
        n = len(x)
        J = np.zeros((n, n))
        for i in range(n):
            x_plus = x.copy()
            x_minus = x.copy()
            x_plus[i] += self.h
            x_minus[i] -= self.h
            J[:, i] = (func(x_plus) - func(x_minus)) / (2 * self.h)
        return J

    def solve(self,
            func: Callable[[np.ndarray], np.ndarray],
            initial_guess: np.ndarray) -> Tuple[np.ndarray, int]:
        """
        Find root of a system of equations using Newton's method with divergence detection and numerical differentiation.

        Args:
            func (Callable[[np.ndarray], np.ndarray]): The system of equations to solve
            initial_guess (np.ndarray): The initial guess for the solution

        Returns:
            Tuple[np.ndarray, int]: The solution and the number of iterations

        Raises:
            TypeError: If the function is not callable
            ValueError: If the solution diverges, fails to converge, or encounters a singular Jacobian
        """
        if not callable(func):
            raise TypeError("Function must be callable")

        x = initial_guess
        for iterations in range(self.max_iterations):
            fx = func(x)

            # Check convergence
            if np.linalg.norm(fx) < self.tolerance:
                return x, iterations

            # Check divergence
            if np.linalg.norm(x) > self.divergence_threshold:
                raise ValueError(f"Solution diverged after {iterations} iterations")

            # Compute Jacobian numerically
            J = self.numerical_jacobian(func, x)

            # Check for singular Jacobian
            if np.linalg.cond(J) > 1 / np.finfo(float).eps:
                raise ValueError(f"Encountered singular Jacobian at iteration {iterations}")

            # Solve linear system J * delta_x = -fx
            try:
                delta_x = np.linalg.solve(J, -fx)
            except np.linalg.LinAlgError:
                raise ValueError(f"Failed to solve linear system at iteration {iterations}")

            # Newton's method update
            x = x + delta_x

        raise ValueError(f"Failed to converge after {self.max_iterations} iterations")