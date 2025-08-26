# auto_gmail_creator/cli.py
import os
import sys
import click
from rich.console import Console
from rich.table import Table

from .generator import AccountGenerator
from .utils import export_to_csv, export_to_json

console = Console()

MAX_ALLOWED = 1000  # soft guardrail for bulk runs


@click.group()
def cli():
    """Auto Gmail Creator ✨ - A simulation tool for bulk Gmail account creation."""
    pass


@cli.command()
@click.option(
    "-c",
    "--count",
    default=5,
    type=int,
    help="Number of simulated accounts to generate.",
    show_default=True,
)
@click.option(
    "-o",
    "--output",
    type=click.Choice(["json", "csv"]),
    help="Export the generated accounts to a file (JSON or CSV).",
)
@click.option(
    "--output-path",
    type=click.Path(file_okay=True, dir_okay=False, writable=True, path_type=str),
    help="Optional path (including filename) for export. Overrides default filename.",
)
@click.option(
    "--password-length",
    default=12,
    show_default=True,
    type=click.IntRange(8, 128),
    help="Length for generated passwords.",
)
@click.option(
    "--seed",
    type=int,
    help="Optional seed for reproducible names/usernames (passwords remain random).",
)
@click.option(
    "--bypass-verification",
    is_flag=True,
    help="[DEMO-ONLY] Mark phone verification as true in the output (no real effect).",
)
@click.option(
    "--acknowledge-simulation",
    is_flag=True,
    help="Acknowledge this tool is a simulation ONLY (adds friction & clarity).",
)
def generate(count, output, output_path, password_length, seed, bypass_verification, acknowledge_simulation):
    """Generates simulated Gmail accounts."""

    if count > MAX_ALLOWED:
        console.print(f"[bold red]Refusing to generate more than {MAX_ALLOWED} in one run.[/bold red]")
        raise SystemExit(2)

    banner = (
        "[bold yellow]⚠️  Disclaimer: Simulation tool for educational/testing purposes only.[/bold yellow]\n"
        "[bold yellow]It does NOT create real Gmail accounts, interact with Google, "
        "or bypass security measures.[/bold yellow]\n"
    )
    console.print(banner)

    if not acknowledge_simulation and not os.environ.get("AGC_I_UNDERSTAND_SIMULATION"):
        console.print(
            "[dim]Tip: pass --acknowledge-simulation (or set AGC_I_UNDERSTAND_SIMULATION=1) to suppress this reminder.[/dim]\n"
        )

    generator = AccountGenerator(seed=seed)
    accounts = []

    with console.status(
        f"[bold green]Simulating creation of {count} accounts...[/bold green]"
    ) as status:
        for i in range(count):
            account = generator.generate_account(password_length=password_length)
            if bypass_verification:
                account = generator.simulate_phone_verification_bypass(account)
            accounts.append(account)
            status.update(
                f"[bold green]Generated account {i + 1}/{count}: {account['email']}[/bold green]"
            )

    console.print("\n[bold green]✅ Simulated Account Generation Complete![/bold green]")

    # Display results in a table
    table = Table(title="Generated Gmail Accounts (Simulated)", show_lines=False)
    table.add_column("First Name", style="cyan")
    table.add_column("Last Name", style="cyan")
    table.add_column("Email", style="magenta")
    table.add_column("Password", style="yellow")
    table.add_column("Recovery Email", style="blue")
    table.add_column("Verified", style="green")

    for acc in accounts:
        table.add_row(
            acc["first_name"],
            acc["last_name"],
            acc["email"],
            acc["password"],
            acc["recovery_email"],
            "✅ [DEMO]" if acc["phone_verified"] else "❌",
        )

    console.print(table)

    # Export if requested
    if output:
        if output_path:
            filename = output_path
        else:
            filename = f"generated_accounts.{output}"

        if output == "json":
            export_to_json(accounts, filename)
        else:
            export_to_csv(accounts, filename)

        console.print(
            f"\n[bold green]Successfully exported accounts to [cyan]{filename}[/cyan].[/bold green]"
        )


if __name__ == "__main__":
    cli()
