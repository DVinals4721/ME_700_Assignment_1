import math
import pytest
from root_finding_methods import NewtonMethodSolver

class TestNewtonMethodSolver:
    def setup_method(self):
        self.solver = NewtonMethodSolver()

    def test_polynomial_root(self):
        def f(x): return x**2 - 4
        def df(x): return 2*x

        root, iterations = self.solver.solve(f, df, 3)
        assert math.isclose(root, 2, abs_tol=1e-6)

    def test_trigonometric_root(self):
        def f(x): return math.sin(x)
        def df(x): return math.cos(x)

        root, iterations = self.solver.solve(f, df, 3)
        assert math.isclose(root, math.pi, abs_tol=1e-6)

    def test_invalid_inputs(self):
        with pytest.raises(TypeError):
            self.solver.solve("not func", lambda x: x, 0)

    def test_incorrect_derivative(self):
        def f(x):
            return x ** 2 - 2  # Example function x^2 - 2

        def incorrect_df(x):
            return x  # Incorrect derivative (should be 2x, but it's x)


        # Use pytest.raises to check that ValueError is raised for incorrect derivative
        with pytest.raises(ValueError):
            self.solver.solve(f, incorrect_df, initial_guess=1.0)