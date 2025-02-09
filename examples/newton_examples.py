import math
from root_finding_methods import NewtonMethodSolver

def run_tutorial_examples():
    solver = NewtonMethodSolver(max_iterations=50, tolerance=1e-6, divergence_threshold=1e10, h=1e-7)

    # 1. Polynomial root finding
    def polynomial(x):
        return x**3 - x - 2

    try:
        root, iterations = solver.solve(polynomial, 1.5)
        print(f"1. Polynomial Root: {root} (iterations: {iterations})")
    except ValueError as e:
        print(f"1. Polynomial Root: Error - {str(e)}")

    # 2. Trigonometric equation
    def trig(x):
        return math.tan(x) - 1

    try:
        root, iterations = solver.solve(trig, 0.7)
        print(f"2. Trigonometric Root: {root} (iterations: {iterations})")
    except ValueError as e:
        print(f"2. Trigonometric Root: Error - {str(e)}")

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

    try:
        root, iterations = solver.solve(beam_deflection, 1000)
        print(f"3. Beam Deflection Load: {root:.2f} N (iterations: {iterations})")
    except ValueError as e:
        print(f"3. Beam Deflection Load: Error - {str(e)}")

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

    try:
        root, iterations = solver.solve(stress_concentration, 2.0)
        print(f"4. Stress Concentration Factor: {root:.2f} (iterations: {iterations})")
    except ValueError as e:
        print(f"4. Stress Concentration Factor: Error - {str(e)}")

    # 5. Exponential equation
    def exponential(x):
        return math.exp(x) - 5*x

    try:
        root, iterations = solver.solve(exponential, 2.0)
        print(f"5. Exponential Equation Root: {root} (iterations: {iterations})")
    except ValueError as e:
        print(f"5. Exponential Equation Root: Error - {str(e)}")

if __name__ == "__main__":
    run_tutorial_examples()