import math
import pytest
from root_finding_methods import BisectionSolver

class TestBisectionSolver:
    """
    Comprehensive test suite for the BisectionSolver class.

    Tests cover various scenarios including:
    - Successful root finding
    - Error handling
    - Edge cases
    """

    def setup_method(self):
        """Create a fresh BisectionSolver for each test"""
        self.solver = BisectionSolver()

    def test_simple_polynomial_root(self):
        """Test finding root of a simple polynomial"""
        def test_func(x):
            return x**2 - 4  # Root at x = ±2

        root, iterations = self.solver.solve(test_func, 0, 3)
        assert math.isclose(root, 2, abs_tol=1e-6)
        assert iterations < 100

    def test_trigonometric_function(self):
        """Test finding root of a trigonometric function"""
        def test_func(x):
            return math.sin(x)

        root, iterations = self.solver.solve(test_func, 3, 4)
        assert math.isclose(root, math.pi, abs_tol=1e-6)
        assert iterations < 100

    def test_invalid_interval(self):
        """Test that an error is raised when root cannot be bracketed"""
        def test_func(x):
            return x**2 + 1  # No real roots

        with pytest.raises(ValueError, match="Root cannot be bracketed"):
            self.solver.solve(test_func, -1, 1)

    def test_non_callable_input(self):
        """Test error handling for non-callable input"""
        with pytest.raises(TypeError, match="Input must be a callable function"):
            self.solver.solve("not a function", 0, 1)

    def test_invalid_solver_configuration(self):
        """Test constructor error handling"""
        with pytest.raises(ValueError, match="Max iterations must be a positive integer"):
            BisectionSolver(max_iterations=0)

        with pytest.raises(ValueError, match="Tolerance must be a positive float"):
            BisectionSolver(tolerance=-0.1)