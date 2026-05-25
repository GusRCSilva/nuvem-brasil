"""List all specs with green/red status based on test results."""
from __future__ import annotations

import glob
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rich.console import Console
from rich.table import Table

console = Console()


def test_file_for_spec(spec_path: str) -> str | None:
    rel = os.path.relpath(spec_path, "specs/features")
    dir_part, stem = os.path.split(rel)
    test_name = f"test_{dir_part.replace(os.sep, '_')}_{os.path.splitext(stem)[0]}.py"
    test_path = os.path.join("tests", "from_specs", test_name)
    return test_path if os.path.exists(test_path) else None


def run_test(test_path: str) -> bool:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", test_path, "-q", "--no-header"],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def list_specs() -> int:
    spec_files = sorted(glob.glob("specs/features/**/*.spec.yaml", recursive=True))
    if not spec_files:
        console.print("[yellow]No specs found.[/yellow]")
        return 0

    table = Table(title="Spec Status")
    table.add_column("Spec", style="cyan")
    table.add_column("Test File", style="dim")
    table.add_column("Status")

    all_green = True
    for spec_path in spec_files:
        test_path = test_file_for_spec(spec_path)
        if test_path:
            passing = run_test(test_path)
            status = "[green]✓ green[/green]" if passing else "[red]✗ red[/red]"
            test_display = test_path
            if not passing:
                all_green = False
        else:
            status = "[red]✗ red[/red]"
            test_display = "[red]missing[/red]"
            all_green = False

        table.add_row(spec_path, test_display, status)

    console.print(table)
    return 0 if all_green else 1


def main() -> None:
    sys.exit(list_specs())


if __name__ == "__main__":
    main()
