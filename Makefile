.PHONY: install lint test

install:
	pip install -r requirements.txt

lint:
	ruff src

format:
	black src

test:
	pytest

nbtest:
	pytest --nbval stats.ipynb
