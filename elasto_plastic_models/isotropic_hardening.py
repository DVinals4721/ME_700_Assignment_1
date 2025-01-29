import numpy as np
from root_finding_methods import BisectionSolver

class IsotropicHardeningModel:
    def __init__(self, E, sigma_y, K, n):
        """
        Initialize the Isotropic Hardening Model.
        
        Args:
        E (float): Young's modulus
        sigma_y (float): Initial yield stress
        K (float): Strength coefficient
        n (float): Strain hardening exponent
        """
        self.E = E
        self.sigma_y = sigma_y
        self.K = K
        self.n = n
        self.plastic_strain = 0
        self.current_yield_stress = sigma_y
        self.solver = BisectionSolver(max_iterations=1000, tolerance=1e-6)

    def calculate_stress(self, total_strain):
        """
        Calculate stress given total strain.
        
        Args:
        total_strain (float): Total strain

        Returns:
        float: Calculated stress
        """
        trial_stress = self.E * (total_strain - self.plastic_strain)
        
        if abs(trial_stress) <= self.current_yield_stress:
            return trial_stress
        else:
            # Solve for plastic strain increment
            def yield_function(d_ep):
                return abs(self.E * (total_strain - self.plastic_strain - d_ep)) - (self.sigma_y + self.K * (self.plastic_strain + d_ep)**self.n)
            
            # Use bisection method to find d_ep
            d_ep, _ = self.solver.solve(yield_function, 0, total_strain - self.plastic_strain)
            
            self.plastic_strain += d_ep
            self.current_yield_stress = self.sigma_y + self.K * self.plastic_strain**self.n
            
            return np.sign(trial_stress) * self.current_yield_stress

    def reset(self):
        """Reset the model to its initial state."""
        self.plastic_strain = 0
        self.current_yield_stress = self.sigma_y

    def get_current_yield_stress(self):
        """
        Get the current yield stress.

        Returns:
        float: Current yield stress
        """
        return self.current_yield_stress

    def get_plastic_strain(self):
        """
        Get the current plastic strain.

        Returns:
        float: Current plastic strain
        """
        return self.plastic_strain