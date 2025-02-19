import math
import numpy as np
from root_finding_methods import NewtonMethodSolver

def run_tutorial_examples():
    solver = NewtonMethodSolver(max_iterations=50, tolerance=1e-6, divergence_threshold=1e10, h=1e-7)

    # 1. System of two equations
    def system1(x):
        return np.array([
            x[0]**2 + x[1]**2 - 1,  # x^2 + y^2 = 1
            x[0] - x[1]             # x = y
        ])

    try:
        root, iterations = solver.solve(system1, np.array([0.5, 0.5]))
        print(f"1. System 1 Root: {root} (iterations: {iterations})")
    except ValueError as e:
        print(f"1. System 1 Root: Error - {str(e)}")

    # 2. Nonlinear system
    def system2(x):
        return np.array([
            np.sin(x[0]) + x[1]**2 - 1,
            x[0]**2 + np.cos(x[1]) - 1
        ])

    try:
        root, iterations = solver.solve(system2, np.array([0.5, 0.5]))
        print(f"2. Nonlinear System Root: {root} (iterations: {iterations})")
    except ValueError as e:
        print(f"2. Nonlinear System Root: Error - {str(e)}")

    # 3. Mechanics: Truss Analysis
    def truss_system(x):
        """
        Analyze a simple 3-bar truss
        F = applied force (known)
        θ = angle of the inclined members (known)
        x[0] = T1 (tension in member 1)
        x[1] = T2 (tension in member 2)
        x[2] = T3 (tension in member 3)
        """
        F = 1000  # N
        theta = np.radians(60)  # 60 degrees
        return np.array([
            x[0] * np.cos(theta) + x[1] - F,  # Sum of forces in x-direction
            x[0] * np.sin(theta) - x[2],  # Sum of forces in y-direction
            x[0] * np.cos(theta) - x[1] * np.cos(theta)  # Moment about right support
        ])

    try:
        root, iterations = solver.solve(truss_system, np.array([500, 500, 500]))
        print(f"3. Truss Analysis: T1 = {root[0]:.2f} N, T2 = {root[1]:.2f} N, T3 = {root[2]:.2f} N (iterations: {iterations})")
    except ValueError as e:
        print(f"3. Truss Analysis: Error - {str(e)}")

    # 4. Chemical Equilibrium
    def chemical_equilibrium(x):
        """
        Find equilibrium concentrations in a chemical reaction
        A + 2B ⇌ C
        K_eq = [C] / ([A][B]^2) = 10
        Initial concentrations: [A]_0 = 1 M, [B]_0 = 2 M, [C]_0 = 0 M
        x[0] = [A], x[1] = [B], x[2] = [C]
        """
        K_eq = 10
        return np.array([
            x[0] + x[2] - 1,  # [A] + [C] = [A]_0
            x[1] + 2*x[2] - 2,  # [B] + 2[C] = [B]_0
            K_eq * x[0] * x[1]**2 - x[2]  # K_eq * [A][B]^2 = [C]
        ])

    try:
        root, iterations = solver.solve(chemical_equilibrium, np.array([0.5, 1.0, 0.5]))
        print(f"4. Chemical Equilibrium: [A] = {root[0]:.4f}, [B] = {root[1]:.4f}, [C] = {root[2]:.4f} (iterations: {iterations})")
    except ValueError as e:
        print(f"4. Chemical Equilibrium: Error - {str(e)}")

    # 5. Mechanics: Beam with Spring Support
    def beam_spring_system(x):
        """
        Analyze a beam with a spring support
        F = applied force (known)
        L = beam length (known)
        k = spring stiffness (known)
        x[0] = R1 (reaction force at left support)
        x[1] = R2 (reaction force at right support)
        x[2] = δ (deflection at spring location)
        """
        F = 1000  # N
        L = 5  # m
        k = 2000  # N/m
        a = L / 2  # Spring location (middle of beam)
        return np.array([
            x[0] + x[1] + k*x[2] - F,  # Sum of forces
            x[0] * L + k * x[2] * a - F * a,  # Moment about right support
            x[2] - (F*a*(L-a)**2 / (3*L) - x[0]*a**2*(L-a) / (3*L)) / (k*L)  # Deflection equation
        ])

    try:
        root, iterations = solver.solve(beam_spring_system, np.array([500, 500, 0.01]))
        print(f"5. Beam with Spring: R1 = {root[0]:.2f} N, R2 = {root[1]:.2f} N, δ = {root[2]:.4f} m (iterations: {iterations})")
    except ValueError as e:
        print(f"5. Beam with Spring: Error - {str(e)}")

if __name__ == "__main__":
    run_tutorial_examples()