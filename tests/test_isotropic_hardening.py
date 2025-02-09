import pytest
import numpy as np
from elasto_plastic_models import IsotropicHardeningModel
@pytest.fixture
def model():
    return IsotropicHardeningModel(E=200000, sigma_y=250, K=1500, n=0.3)

def test_initial_state(model):
    assert model.get_current_yield_stress() == 250
    assert model.get_plastic_strain() == 0

def test_elastic_loading(model):
    stress = model.calculate_stress(0.001)  # 0.1% strain, should be elastic
    assert np.isclose(stress, 200)  # 200000 * 0.001 = 200 MPa
    assert model.get_plastic_strain() == 0

def test_initial_yield(model):
    stress = model.calculate_stress(0.00125)  # Just at yield point
    assert np.isclose(stress, 250, rtol=1e-3)
    assert model.get_plastic_strain() < 1e-6

def test_plastic_loading(model):
    stress = model.calculate_stress(0.02)  # 2% strain, should be plastic
    assert stress > 250
    assert model.get_plastic_strain() > 0

def test_unloading(model):
    model.calculate_stress(0.02)  # Load to 2% strain
    initial_plastic_strain = model.get_plastic_strain()
    stress = model.calculate_stress(0.015)  # Unload to 1.5% strain
    assert np.isclose(model.get_plastic_strain(), initial_plastic_strain)
    assert stress < model.get_current_yield_stress()

def test_reloading(model):
    model.calculate_stress(0.02)  # Load to 2% strain
    model.calculate_stress(0.015)  # Unload to 1.5% strain
    stress = model.calculate_stress(0.025)  # Reload to 2.5% strain
    assert stress >= model.get_current_yield_stress()
    assert model.get_plastic_strain() > 0.02 - 250/200000  # Approximate check

def test_reset(model):
    model.calculate_stress(0.02)  # Load to 2% strain
    model.reset()
    assert model.get_current_yield_stress() == 250
    assert model.get_plastic_strain() == 0


def test_cyclic_loading(model):
    stresses = []
    strains = [0, 0.02, -0.02, 0.02, 0]
    for strain in strains:
        stresses.append(model.calculate_stress(strain))
    assert len(set(map(abs, stresses))) > 1  # Check for Bauschinger effect

def test_large_strain(model):
    stress = model.calculate_stress(0.1)  # 10% strain
    assert stress >= model.get_current_yield_stress()
    assert model.get_plastic_strain() > 0.09  # Approximate check

if __name__ == "__main__":
    pytest.main()