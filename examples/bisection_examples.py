import math
import sys
import os
import math
from root_finding_methods import BisectionSolver

def run_tutorial_examples():
    """
    Demonstrate bisection method solver with various problem types.

    Examples cover:
    1. Simple polynomial root finding
    2. Trigonometric equation
    3. Exponential function
    4. Mechanics problem: Free fall time
    5. Mechanics problem: Projectile motion
    """
    # Initialize solver with custom parameters
    solver = BisectionSolver(max_iterations=500, tolerance=1e-3)

    # Example 1: Polynomial Root Finding
    def polynomial(x):
        """Solve x³ - x - 2 = 0"""
        return x**3 - x - 2

    root, iterations = solver.solve(polynomial, 1, 2)
    print(f"Polynomial Root: {root} (iterations: {iterations})")

    # Example 2: Trigonometric Equation
    def trig_equation(x):
        """Solve tan(x) = 1"""
        return math.tan(x) - 1

    root, iterations = solver.solve(trig_equation, 0, math.pi/2)
    print(f"Trigonometric Root: {root} (iterations: {iterations})")

    # Example 3: Exponential Function
    def exponential(x):
        """Solve e^x - 3x = 0"""
        return math.exp(x) - 3*x

    root, iterations = solver.solve(exponential, 0, 1)
    print(f"Exponential Root: {root} (iterations: {iterations})")

    # Example 4: Mechanics - Free Fall Time
    def free_fall_time(t):
        """
        Find time when object reaches 50m in free fall
        h = 0.5 * g * t²
        g ≈ 9.8 m/s²
        """
        g = 9.8
        return 0.5 * g * t**2 - 50

    root, iterations = solver.solve(free_fall_time, 0, 5)
    print(f"Free Fall Time: {root}s (iterations: {iterations})")

    # Example 5: Mechanics - Spring Oscillation
    def spring_position(t):
        """
        Find time when spring displacement is exactly zero
        Simplified spring model with damping
        """
        amplitude = 1.0  # initial displacement
        damping = 0.2    # damping coefficient
        frequency = 2.0  # natural frequency

        return amplitude * math.exp(-damping * t) * math.cos(frequency * t)

    root, iterations = solver.solve(spring_position, 0, 5)
    print(f"Spring Zero Crossing: {root}s (iterations: {iterations})")

if __name__ == "__main__":
    run_tutorial_examples()