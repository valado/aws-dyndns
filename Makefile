# Setup dedicated virtual python environment
init:
	python3 -m venv .venv

# Activate virtual environment
activate:
	. .venv/bin/activate

# Deactivate virtual environment
deactivate:
	deactivate

# Install dependencies
install:
	pip install -r requirements.txt

# Run
run:
	python3 ddns.py

# Save dependencies
save:
	pip3 freeze > requirements.txt

# Update dependencies
update:
	pip-review --local --auto

# Check if dependencies are met
check:
	python -m pip check

# Run tests
test:
	nosetests tests