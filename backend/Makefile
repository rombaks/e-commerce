lint:
	black --check .
	flake8
	isort --check-only .

test:
	python -m pytest

check: lint test

format_code:
	isort .
	black .
