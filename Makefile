# Variables
VENV := venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

# Main target that runs all scripts
all: run

# Main Scripts:
run: $(VENV)
	time $(PYTHON) ./main.py

# Individual script targets
chatgpt: $(VENV)
	time $(PYTHON) ./chatgpt.py

copilot: $(VENV)
	time $(PYTHON) ./copilot.py

gemini: $(VENV)
	time $(PYTHON) ./gemini.py

llama: $(VENV)
	time $(PYTHON) ./llama.py

mistral: $(VENV)
	time $(PYTHON) ./mistral.py

# Setup Virtual Environment and Install Dependencies
$(VENV):
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

# Install the project dependencies
dependencies: $(VENV)

# Generate requirements.txt from the current venv
generate_requirements: $(VENV)
	$(PIP) freeze > requirements.txt

# Utility rule for cleaning the project
clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

.PHONY: all run chatgpt copilot gemini llama mistral clean dependencies generate_requirements
