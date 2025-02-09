# ME_700_Assignments

This package provides implementations of advanced engineering computational methods, including:

- Root-finding algorithms:
  - Newton's method
  - Bisection method
- Elasto-plastic material models:
  - Kinematic hardening
  - Isotropic hardening

# Installation and Testing

## Prerequisites
- Git
- Conda (or Mamba)
- Python 3.12

## Steps

1. **Clone the repository:**
      bash

      git clone https://github.com/DVinals4721/ME_700_Assignments.git

      cd ME_700_Assignments

2. **Set up a Conda environment:**

    conda create --name me-700-env python=3.12
    conda activate me-700-env

Note: You can also use mamba if you prefer.

3. **Verify Python version:**

    python --version

Ensure it shows version 3.12.

4. **Update pip and essential tools:**

    pip install --upgrade pip setuptools wheel

5. **Install the package in editable mode:**

    pip install -e .

Make sure you're in the correct directory (ME_700_Assignments) when running this command.

6. **Install pytest and pytest-cov for testing:**

    pip install pytest pytest-cov

7. **Run tests with coverage:**

    pytest -v --cov=root_finding_methods --cov-report term-missing

**Usage Examples**

After installation, explore the functionality through our example scripts:

Newton's Method

    python examples/newton_example.py

Bisection Method

    python examples/bisection_example.py

Kinematic Hardening Model

    python examples/kinematic_hardening_example.py

Isotropic Hardening Model

    python examples/isotropic_hardening_example.py

