.PHONY: install test lint format ci

install:
	pip install -r requirements.txt
	pip install pylint isort pytest

test:
	pytest

lint:
	pylint app tests

format:
	isort app tests

ci: install format lint test
