"""Validate all spec YAML files against the Pydantic schema."""
from __future__ import annotations

import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml
from rich.console import Console

from specs.schema.spec_schema import Spec

console = Console()


def validate_all() -> int:
    spec_files = sorted(glob.glob("specs/features/**/*.spec.yaml", recursive=True))
    if not spec_files:
        console.print("[yellow]No spec files found.[/yellow]")
        return 0

    errors = 0
    for path in spec_files:
        try:
            with open(path) as f:
                data = yaml.safe_load(f)
            Spec.model_validate(data)
            console.print(f"[green]✓[/green] {path}")
        except Exception as e:
            console.print(f"[red]✗[/red] {path}: {e}")
            errors += 1

    return 0 if errors == 0 else 1


def main() -> None:
    sys.exit(validate_all())


if __name__ == "__main__":
    main()
