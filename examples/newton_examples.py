import math
from root_finding_methods import NewtonMethodSolver

def run_tutorial_examples():
    solver = NewtonMethodSolver(max_iterations=50, tolerance=1e-6)

    # 1. Polynomial root finding
    def polynomial(x):
        return x**3 - x - 2
    def polynomial_deriv(x):
        return 3*x**2 - 1

    root, iterations = solver.solve(polynomial, polynomial_deriv, 1.5)
    print(f"1. Polynomial Root: {root} (iterations: {iterations})")

    # 2. Trigonometric equation
    def trig(x):
        return math.tan(x) - 1
    def trig_deriv(x):
        return 1 / (math.cos(x)**2)

    root, iterations = solver.solve(trig, trig_deriv, 0.7)
    print(f"2. Trigonometric Root: {root} (iterations: {iterations})")

    # 3. Mechanics of Materials: Beam Deflection
    def beam_deflection(P):
        """
        Find load P that causes a specific deflection in a cantilever beam
        Deflection equation: δ = PL^3 / (3EI)
        Target deflection: 0.05 m
        L = 2 m, E = 200 GPa, I = 1e-6 m^4
        """
        L, E, I = 2, 200e9, 1e-6
        return (P * L**3) / (3 * E * I) - 0.05

    def beam_deflection_deriv(P):
        L, E, I = 2, 200e9, 1e-6
        return (L**3) / (3 * E * I)

    root, iterations = solver.solve(beam_deflection, beam_deflection_deriv, 1000)
    print(f"3. Beam Deflection Load: {root:.2f} N (iterations: {iterations})")

    # 4. Mechanics of Materials: Stress Concentration
    def stress_concentration(K):
        """
        Find stress concentration factor K that results in a specific max stress
        Stress equation: σ_max = K * σ_nom
        Target max stress: 300 MPa
        Nominal stress: 100 MPa
        """
        sigma_nom = 100e6  # 100 MPa
        return K * sigma_nom - 300e6

    def stress_concentration_deriv(K):
        return 100e6  # derivative of K * σ_nom with respect to K

    root, iterations = solver.solve(stress_concentration, stress_concentration_deriv, 1000)
    print(f"4. Stress Concentration Factor: {root:.2f} (iterations: {iterations})")

    # 5. Exponential equation
    def exponential(x):
        return math.exp(x) - 5*x
    def exponential_deriv(x):
        return math.exp(x) - 5

    root, iterations = solver.solve(exponential, exponential_deriv, 2.0)
    print(f"5. Exponential Equation Root: {root} (iterations: {iterations})")

if __name__ == "__main__":
    run_tutorial_examples()