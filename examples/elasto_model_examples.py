# examples/tutorial.py

import numpy as np
from elasto_plastic_models import KinematicHardeningModel
from elasto_plastic_models import IsotropicHardeningModel

def print_results(strains, stresses, title):
    print(f"\n{title}")
    print("-" * 50)
    print("Strain\t\tStress")
    print("-" * 50)
    for strain, stress in zip(strains[::10], stresses[::10]):  # Print every 10th value
        print(f"{strain:.4f}\t\t{stress:.2f}")
    print("-" * 50)
    print(f"Max Strain: {max(strains):.4f}")
    print(f"Max Stress: {max(stresses):.2f}")
    print(f"Min Strain: {min(strains):.4f}")
    print(f"Min Stress: {min(stresses):.2f}")

# Example 1: Uniaxial tension with kinematic hardening
def example_1():
    model = KinematicHardeningModel(E=200e3, sigma_y=250, H=10e3)
    strains = np.linspace(0, 0.02, 100)
    stresses = [model.calculate_stress(strain) for strain in strains]
    print_results(strains, stresses, "Uniaxial Tension - Kinematic Hardening")

# Example 2: Cyclic loading with kinematic hardening
def example_2():
    model = KinematicHardeningModel(E=200e3, sigma_y=250, H=10e3)
    strains = np.concatenate([np.linspace(0, 0.02, 50), np.linspace(0.02, -0.02, 100), np.linspace(-0.02, 0, 50)])
    stresses = [model.calculate_stress(strain) for strain in strains]
    print_results(strains, stresses, "Cyclic Loading - Kinematic Hardening")

# Example 3: Uniaxial tension with isotropic hardening
def example_3():
    model = IsotropicHardeningModel(E=200e3, sigma_y=250, K=500, n=0.1)
    strains = np.linspace(0, 0.05, 100)
    stresses = [model.calculate_stress(strain) for strain in strains]
    print_results(strains, stresses, "Uniaxial Tension - Isotropic Hardening")

# Example 4: Stress relaxation with kinematic hardening
def example_4():
    model = KinematicHardeningModel(E=200e3, sigma_y=250, H=10e3)
    initial_strain = 0.015
    times = np.linspace(0, 1000, 100)
    relaxation_rate = 1e-5
    stresses = []
    for t in times:
        strain = initial_strain - relaxation_rate * t
        stresses.append(model.calculate_stress(strain))
    print_results(times, stresses, "Stress Relaxation - Kinematic Hardening")

# Example 5: Comparison of kinematic and isotropic hardening
def example_5():
    kin_model = KinematicHardeningModel(E=200e3, sigma_y=250, H=10e3)
    iso_model = IsotropicHardeningModel(E=200e3, sigma_y=250, K=500, n=0.1)
    strains = np.linspace(0, 0.05, 100)
    kin_stresses = [kin_model.calculate_stress(strain) for strain in strains]
    iso_stresses = [iso_model.calculate_stress(strain) for strain in strains]
    
    print("\nComparison of Hardening Models")
    print("-" * 50)
    print("Strain\t\tKinematic\tIsotropic")
    print("-" * 50)
    for strain, kin_stress, iso_stress in zip(strains[::10], kin_stresses[::10], iso_stresses[::10]):
        print(f"{strain:.4f}\t\t{kin_stress:.2f}\t\t{iso_stress:.2f}")
    print("-" * 50)
    print(f"Max Kinematic Stress: {max(kin_stresses):.2f}")
    print(f"Max Isotropic Stress: {max(iso_stresses):.2f}")

if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()