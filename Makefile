.PHONY: install test lint format ci terraform-init-dev terraform-plan-dev terraform-apply-dev

install:
	pip install -r requirements.txt
	pip install pylint isort pytest black

test:
	PYTHONPATH=. pytest

lint:
	PYTHONPATH=. pylint app tests

format:
	isort app tests
	black app tests

ci: install format lint test

# Terraform helpers (DEV)

terraform-init-dev:
	cd terraform/env/dev && terraform init

terraform-plan-dev:
	cd terraform/env/dev && terraform plan

terraform-apply-dev:
	cd terraform/env/dev && terraform apply -auto-approve
