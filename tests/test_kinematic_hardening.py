# tests/test_kinematic_hardening.py

import pytest
import numpy as np
from elasto_plastic_models import KinematicHardeningModel

@pytest.fixture
def model():
    return KinematicHardeningModel(E=200000, sigma_y=250, H=10000)

def test_initial_state(model):
    assert model.plastic_strain == 0
    assert model.back_stress == 0

def test_elastic_loading(model):
    stress = model.calculate_stress(0.001)  # 0.1% strain, should be elastic
    assert np.isclose(stress, 200)  # 200000 * 0.001 = 200 MPa
    assert model.plastic_strain == 0
    assert model.back_stress == 0

def test_initial_yield(model):
    stress = model.calculate_stress(0.00125)  # Just at yield point
    assert np.isclose(stress, 250, rtol=1e-3)
    assert model.plastic_strain < 1e-6
    assert model.back_stress < 1e-6

def test_plastic_loading(model):
    stress = model.calculate_stress(0.02)  # 2% strain, should be plastic
    assert stress > 250
    assert model.plastic_strain > 0
    assert model.back_stress > 0

def test_reverse_loading(model):
    model.calculate_stress(0.02)  # Load to 2% strain
    stress_positive = model.calculate_stress(0.02)
    stress_negative = model.calculate_stress(-0.02)
    assert abs(stress_negative) <= abs(stress_positive)  # Bauschinger effect

def test_cyclic_loading(model):
    stresses = []
    strains = [0, 0.02, -0.02, 0.02, 0]
    for strain in strains:
        stresses.append(model.calculate_stress(strain))
    assert len(set(map(abs, stresses))) > 1  # Check for Bauschinger effect

def test_reset(model):
    model.calculate_stress(0.02)  # Load to 2% strain
    model.reset()
    assert model.plastic_strain == 0
    assert model.back_stress == 0

def test_large_strain(model):
    stress = model.calculate_stress(0.1)  # 10% strain
    assert stress > 250
    assert model.plastic_strain > 0
    assert model.back_stress > 0

def test_stress_strain_curve(model):
    strains = np.linspace(0, 0.05, 100)
    stresses = [model.calculate_stress(strain) for strain in strains]
    assert all(np.diff(stresses) >= 0)  # Stress should be non-decreasing

def test_bauschinger_effect_magnitude(model):
    forward_stress = model.calculate_stress(0.02)
    model.reset()
    reverse_stress = abs(model.calculate_stress(-0.02))
    assert reverse_stress <= forward_stress

if __name__ == "__main__":
    pytest.main()