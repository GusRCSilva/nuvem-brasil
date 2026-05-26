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
    uv run pytest apps/email-server/tests/from_specs/test_`echo {{spec_path}} | tr '/' '_'`.py -v

lint:
    uv run ruff check .
    uv run ruff format --check .
    uv run mypy apps shared tools

format:
    uv run ruff format .
    uv run ruff check --fix .

clean:
    -podman compose down -v
    rm -rf .pytest_cache .mypy_cache .ruff_cache
    -find . -not -path './volumes/*' -type d -name __pycache__ -exec rm -rf {} +
    -podman unshare rm -rf volumes/postgres

run:
    uv run uvicorn email_server.api.main:app --reload
