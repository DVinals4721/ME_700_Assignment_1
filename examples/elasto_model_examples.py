import numpy as np
import matplotlib.pyplot as plt
from elasto_plastic_models import KinematicHardeningModel, IsotropicHardeningModel

def print_results(strains, stresses, title):
    # Function to print formatted results
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

def plot_results(x, y, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Example 1: Uniaxial tension with kinematic hardening
def example_1():
    # Create a kinematic hardening model
    model = KinematicHardeningModel(E=200e3, sigma_y=250, H=10e3)
    # Generate strain values from 0 to 0.02
    strains = np.linspace(0, 0.02, 100)
    # Calculate stresses for each strain value
    stresses = [model.calculate_stress(strain) for strain in strains]
    
    print_results(strains, stresses, "Uniaxial Tension - Kinematic Hardening")
    plot_results(strains, stresses, "Uniaxial Tension - Kinematic Hardening", "Strain", "Stress (MPa)")

def example_2():
    # Create a kinematic hardening model
    model = KinematicHardeningModel(E=200e3, sigma_y=250, H=10e3)
    
    # Generate strain values for multiple cycles with increasing amplitude
    cycles = 1
    max_strain = 0.05
    points_per_cycle = 200
    strains = []
    for i in range(cycles):
        cycle_max_strain = (i + 1) * max_strain / cycles
        cycle_strains = np.concatenate([
            np.linspace(0, cycle_max_strain, points_per_cycle // 4),
            np.linspace(cycle_max_strain, -cycle_max_strain, points_per_cycle // 2),
            np.linspace(-cycle_max_strain, 0, points_per_cycle // 4)
        ])
        strains.extend(cycle_strains)
    
    strains = np.array(strains)
    
    # Calculate stresses for each strain value
    stresses = [model.calculate_stress(strain) for strain in strains]
    
    print_results(strains, stresses, "Cyclic Loading - Kinematic Hardening")
    plot_results(strains, stresses, "Cyclic Loading - Kinematic Hardening", "Strain", "Stress (MPa)")

    # Plot stress-strain curve
    plt.figure(figsize=(10, 6))
    plt.plot(strains, stresses)
    plt.title("Cyclic Loading - Kinematic Hardening")
    plt.xlabel("Strain")
    plt.ylabel("Stress (MPa)")
    plt.grid(True)
    plt.show()

    # Plot stress and strain vs. time
    time = np.arange(len(strains))
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(time, strains)
    plt.title("Strain vs. Time")
    plt.ylabel("Strain")
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(time, stresses)
    plt.title("Stress vs. Time")
    plt.xlabel("Time")
    plt.ylabel("Stress (MPa)")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Example 3: Uniaxial tension with isotropic hardening
def example_3():
    # Create an isotropic hardening model
    model = IsotropicHardeningModel(E=200e3, sigma_y=250, K=500, n=0.1)
    # Generate strain values from 0 to 0.05
    strains = np.linspace(0, 0.05, 100)
    # Calculate stresses for each strain value
    stresses = [model.calculate_stress(strain) for strain in strains]
    
    print_results(strains, stresses, "Uniaxial Tension - Isotropic Hardening")
    plot_results(strains, stresses, "Uniaxial Tension - Isotropic Hardening", "Strain", "Stress (MPa)")

# Example 4: Stress relaxation with kinematic hardening
def example_4():
    # Create a kinematic hardening model
    model = KinematicHardeningModel(E=200e3, sigma_y=250, H=10e3)
    initial_strain = 0.015
    # Generate time values from 0 to 1000
    times = np.linspace(0, 1000, 100)
    relaxation_rate = 1e-5
    stresses = []
    for t in times:
        # Calculate strain decreasing over time
        strain = initial_strain - relaxation_rate * t
        # Calculate stress for each strain value
        stresses.append(model.calculate_stress(strain))
    
    print_results(times, stresses, "Stress Relaxation - Kinematic Hardening")
    plot_results(times, stresses, "Stress Relaxation - Kinematic Hardening", "Time", "Stress (MPa)")

# Example 5: Comparison of kinematic and isotropic hardening
def example_5():
    # Create both kinematic and isotropic hardening models
    kin_model = KinematicHardeningModel(E=200e3, sigma_y=250, H=10e3)
    iso_model = IsotropicHardeningModel(E=200e3, sigma_y=250, K=500, n=0.1)
    # Generate strain values from 0 to 0.05
    strains = np.linspace(0, 0.05, 100)
    # Calculate stresses for each model
    kin_stresses = [kin_model.calculate_stress(strain) for strain in strains]
    iso_stresses = [iso_model.calculate_stress(strain) for strain in strains]
    
    # Print comparison results
    print("\nComparison of Hardening Models")
    print("-" * 50)
    print("Strain\t\tKinematic\tIsotropic")
    print("-" * 50)
    for strain, kin_stress, iso_stress in zip(strains[::10], kin_stresses[::10], iso_stresses[::10]):
        print(f"{strain:.4f}\t\t{kin_stress:.2f}\t\t{iso_stress:.2f}")
    print("-" * 50)
    print(f"Max Kinematic Stress: {max(kin_stresses):.2f}")
    print(f"Max Isotropic Stress: {max(iso_stresses):.2f}")
    
    # Plot the comparison
    plt.figure(figsize=(10, 6))
    plt.plot(strains, kin_stresses, label='Kinematic Hardening')
    plt.plot(strains, iso_stresses, label='Isotropic Hardening')
    plt.title("Comparison of Kinematic and Isotropic Hardening")
    plt.xlabel("Strain")
    plt.ylabel("Stress (MPa)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Run all examples when the script is executed
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()