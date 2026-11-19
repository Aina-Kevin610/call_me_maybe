DIR = $(HOME)/goinfre/call
export UV_CACHE_DIR=$(DIR)/uv_cache
export UV_PROJECT_ENVIRONMENT=$(DIR)/venv
export HF_HOME=$(DIR)/llm

run: install
	uv run python3 -m src \
	--functions_definition data/input/functions_definition.json \
	--input data/input/function_calling_tests.json \
	--output data/output/function_calls.json

install:
	uv sync

lint:
	uv add flake8 mypy
	uv run python3 -m flake8 src/
	uv run python3 -m mypy src/ --warn-return-any
	--warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs
	--check-untyped-defs

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

.PHONY: install run clean lint