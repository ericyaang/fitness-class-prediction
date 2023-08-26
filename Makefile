setup-dir: ## Create the project directory structure
	mkdir data\raw
	mkdir data\processed
	mkdir data\external
	mkdir notebooks\exploratory
	mkdir notebooks\report
	mkdir src
	mkdir tests
	mkdir docker

env:
	@echo "Creating virtual environment"
	python -m venv .venv

activate:
	@echo "Activating virtual environment"
	powershell -noexit -executionpolicy bypass .venv/Scripts/activate.ps1

install:
	@echo "Installing pip, setuptools and requirements"
	python -m pip install --upgrade pip setuptools --no-cache-dir
	python -m pip install -r requirements.txt


.PHONY: setup-dir env activate install
