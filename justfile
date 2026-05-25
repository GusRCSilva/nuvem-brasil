default:
    @just --list

bootstrap:
    uv sync
    uv run pre-commit install

services-up:
    podman compose up -d

services-down:
    podman compose down

spec-validate:
    uv run python tools/spec_validate.py

spec-list:
    uv run python tools/spec_list.py

test *args:
    uv run pytest {{args}}

test-spec spec_path:
    uv run pytest tests/from_specs/test_`echo {{spec_path}} | tr '/' '_'`.py -v

lint:
    uv run ruff check .
    uv run ruff format --check .
    uv run mypy src tools

format:
    uv run ruff format .
    uv run ruff check --fix .

clean:
    -podman compose down -v
    rm -rf .pytest_cache .mypy_cache .ruff_cache
    find . -type d -name __pycache__ -exec rm -rf {} +

run:
    uv run uvicorn gusmail.api.main:app --reload
