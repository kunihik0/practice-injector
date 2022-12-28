.PHONY: format-black
format-black:
	@poetry run black ./src

.PHONY: format-isort
format-isort:
	@poetry run isort ./src

.PHONY: format
format: format-isort format-black

.PHONY: lint-flake8
lint-flake8:
	@poetry run flake8 ./src

.PHONY: lint-mypy
lint-mypy:
	@poetry run mypy ./src

.PHONY: lint
lint: lint-flake8 lint-mypy

.PHONY: test
test:
	@poetry run pytest --cov-config=.coveragerc --cov=src --cov-report=html src
