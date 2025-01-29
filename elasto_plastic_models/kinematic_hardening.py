import numpy as np

class KinematicHardeningModel:
    def __init__(self, E, sigma_y, H):
        self.E = E
        self.sigma_y = sigma_y
        self.H = H
        self.plastic_strain = 0
        self.back_stress = 0

    def calculate_stress(self, total_strain):
        elastic_strain = total_strain - self.plastic_strain
        trial_stress = self.E * elastic_strain
        effective_stress = trial_stress - self.back_stress
        
        if abs(effective_stress) <= self.sigma_y:
            return trial_stress
        else:
            sign = np.sign(effective_stress)
            plastic_strain_increment = (abs(effective_stress) - self.sigma_y) / (self.E + self.H)
            self.plastic_strain += sign * plastic_strain_increment
            self.back_stress += self.H * sign * plastic_strain_increment
            return self.E * (total_strain - self.plastic_strain) + self.back_stress

    def reset(self):
        self.plastic_strain = 0
        self.back_stress = 0