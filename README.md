# ME_700_Assignment_1

This package provides implementations of advanced engineering computational methods, including:

- Root-finding algorithms:
  - Newton's method
  - Bisection method
- Elasto-plastic material models:
  - Kinematic hardening
  - Isotropic hardening

## Installation and Usage


1. Clone the repository:

   ```bash
   git clone https://github.com/DVinals4721/ME_700_Assignment_1.git
   cd ME_700_Assignment_1
   ```

2. Set up a Conda environment:

   ```bash
   conda create --name me-700-env python=3.12
   conda activate me-700-env
   ```

   Note: You can also use mamba if you prefer.

3. Verify Python version:

   ```bash
   python --version
   ```

   Ensure it shows version 3.12.

4. Update pip and essential tools:

   ```bash
   pip install --upgrade pip setuptools wheel
   ```

5. Install the package in editable mode:

   ```bash
   pip install -e .
   ```

   Make sure you're in the correct directory (ME_700_Assignments) when running this command.

6. Install pytest and pytest-cov for testing:

   ```bash
   pip install pytest pytest-cov
   ```

7. Run tests with coverage:

   ```bash
   pytest -v --cov=root_finding_methods --cov-report term-missing
   ```

## Usage Examples

After installation, explore the functionality through our example scripts:

### Newton's Method

```bash
python examples/newton_examples.py
```

### Bisection Method

```bash
python examples/bisection_examples.py
```

### Elasto Model

```bash
python examples/elasto_model_examples.py
```



