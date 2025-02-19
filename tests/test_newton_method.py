import math
import pytest
from root_finding_methods import NewtonMethodSolver
import numpy as np


class TestNewtonMethodSolverSystem:
    def setup_method(self):
        self.solver = NewtonMethodSolver()

    def test_simple_system(self):
        def f(x):
            return np.array([
                x[0]**2 + x[1]**2 - 1,
                x[0] - x[1]
            ])

        root, iterations = self.solver.solve(f, np.array([0.5, 0.5]))
        assert np.allclose(root, np.array([1/np.sqrt(2), 1/np.sqrt(2)]), atol=1e-6)

    def test_nonlinear_system(self):
        def f(x):
            return np.array([
                np.sin(x[0]) + x[1]**2 - 1,
                x[0]**2 + np.cos(x[1]) - 1
            ])

        root, iterations = self.solver.solve(f, np.array([0.5, 0.5]))
        assert np.allclose(f(root), np.zeros(2), atol=1e-6)

    def test_invalid_inputs(self):
        with pytest.raises(TypeError):
            self.solver.solve("not func", np.array([0, 0]))

    def test_non_convergence(self):
        def f(x):
            return np.array([
                np.exp(x[0]) - 1,
                np.exp(x[1]) - 1
            ])

        with pytest.raises(ValueError) as excinfo:
            self.solver.solve(f, np.array([100, 100]))  # Start with large initial guesses
        assert "Failed to converge" in str(excinfo.value)

    def test_singular_jacobian(self):
        def f(x):
            return np.array([
                x[0]**2 - x[1]**2,
                x[0]**2 - x[1]**2
            ])

        try:
            root, iterations = self.solver.solve(f, np.array([1.0, 1.0]))
            # If it doesn't raise an error, check if the solution is valid
            assert np.allclose(f(root), np.zeros(2), atol=1e-6), "Solution does not satisfy the system"
        except Exception as e:
            # If it raises an exception, make sure it's related to the singular Jacobian
            assert "singular" in str(e).lower() or "zero" in str(e).lower(), f"Unexpected error: {str(e)}"

if __name__ == "__main__":
    pytest.main()