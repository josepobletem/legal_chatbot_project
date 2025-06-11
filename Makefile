install:
	pip install -r requirements.txt

test:
	pytest

lint:
	pylint app tests

ci: install lint test
