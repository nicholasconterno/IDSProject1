.PHONY: install lint test

install:
	pip install -r requirements.txt

lint:
	ruff *.py

format:
	black *.py

test:
	pytest

nbtest:
	pytest --nbval stats.ipynb
