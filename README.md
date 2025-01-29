# ME_700_Assignment_1

This package contains implementations of root-finding methods (Newton's method and Bisection method) and elasto-plastic material models (Kinematic and Isotropic hardening).

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:

git clone https://github.com/DVinals4721/me_700_assignment_1.git 

cd me_700_assignment_1


2. Create and activate a virtual environment (optional but recommended):
python -m venv venv source venv/bin/activate # On Windows, use: venv\Scripts\activate


3. Install the package in editable mode:
pip install -e .


## Running Examples

After installation, you can run the example scripts to see the methods in action.

### Newton's Method Example

To run the Newton's method example:

python examples/newton_example.py


### Bisection Method Example

To run the Bisection method example:

python examples/bisection_example.py


### Kinematic Hardening Model Example

To run the Kinematic Hardening model example:

python examples/kinematic_hardening_example.py


### Isotropic Hardening Model Example

To run the Isotropic Hardening model example:

python examples/isotropic_hardening_example.py