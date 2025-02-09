# ME_700_Assignments

This package provides implementations of advanced engineering computational methods, including:

- Root-finding algorithms:
  - Newton's method
  - Bisection method
- Elasto-plastic material models:
  - Kinematic hardening
  - Isotropic hardening

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

    
        git clone https://github.com/DVinals4721/ME_700_Assignment_1.git
        cd ME_700_Assignment_1

2. **Create and activate a virtual environment (optional but recommended):**

        python -m venv venv
        source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. **Install the package in editable mode:**

        pip install -e .

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

