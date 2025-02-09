import math
import pytest
from root_finding_methods import NewtonMethodSolver

class TestNewtonMethodSolver:
    def setup_method(self):
        self.solver = NewtonMethodSolver()

    def test_polynomial_root(self):
        def f(x): return x**2 - 4

        root, iterations = self.solver.solve(f, 3)
        assert math.isclose(root, 2, abs_tol=1e-6)

    def test_trigonometric_root(self):
        def f(x): return math.sin(x)

        root, iterations = self.solver.solve(f, 3)
        assert math.isclose(root, math.pi, abs_tol=1e-6)

    def test_invalid_inputs(self):
        with pytest.raises(TypeError):
            self.solver.solve("not func", 0)

    def test_non_convergence(self):
        def f(x): return math.exp(x) - 1

        with pytest.raises(ValueError) as excinfo:
            self.solver.solve(f, 100)  # Start with a large initial guess
        assert "Failed to converge" in str(excinfo.value)

    def test_near_zero_derivative(self):
        def f(x): return x**3 - x**2

        # This might not raise an error, but should return a result close to the root
        root, iterations = self.solver.solve(f, 1)
        assert math.isclose(root, 0, abs_tol=1e-6) or math.isclose(root, 1, abs_tol=1e-6)

if __name__ == "__main__":
    pytest.main()