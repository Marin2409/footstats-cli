import typer
import readchar
import pyfiglet
from datetime import date, datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Providers 
from src.providers.transfermarket import (
    get_player_transfer_history,
    get_player_profile,
    get_player_stats,
)

from src.providers.threesixtyscore import (
    get_matches
)

# Utils
from src.cli.utils.cli_utils import (
    display_player_profile, 
    display_transfer_history,
    display_stats,
    display_matches,
    select_player,
    version_callback
)

# Init app & console
app = typer.Typer(rich_markup_mode="rich")
console = Console()


# Player Commands ------------------------------------------------------------------
@app.command()
def player(name: str):
    """Search for player and display player profile"""
    selected = select_player(name)
    
    if not selected:
        return
    try:
        profile = get_player_profile(selected.url)
        display_player_profile(profile)
    except Exception as e:
        console.print(f"[bold red]Failed to fetch profile: {e}[/bold red]")

@app.command()
def transfer_history(name: str):
    """Gets Player's Transfer History"""
    selected = select_player(name)
    if not selected:
        return
    try:
        transfers = get_player_transfer_history(selected.url)
        if not transfers:
            console.print("[yellow]No transfer history found.[/yellow]")
            return
        display_transfer_history(transfers)
    except Exception as e:
        console.print(f"[bold red]Failed to fetch transfer history: {e}[/bold red]")

@app.command()
def stats(name: str):
    """Get Player Stats"""
    selected = select_player(name)
    if not selected:
        return
    try:
        stat_rows = get_player_stats(selected.url)
        if not stat_rows:
            console.print("[yellow]No stats found.[/yellow]")
            return
        display_stats(stat_rows)
    except Exception as e:
        console.print(f"[bold red]Failed to fetch stats: {e}[/bold red]")

# Matches Commands ------------------------------------------------------------------
@app.command()
def matches(match_date: str = typer.Argument(
    default=date.today().isoformat(),
    help="Date to fetch matches for (YYYY-MM-DD). Defaults to today."
)):
    """Get football matches for a given date."""
    try:
        parsed_date = datetime.strptime(match_date, "%Y-%m-%d").date()
    except ValueError:
        console.print("[bold red]Invalid date format. Use YYYY-MM-DD (e.g. 2026-06-18)[/bold red]")
        return

    try:
        results = get_matches(parsed_date)
        if not results:
            console.print("[yellow]No matches found for that date.[/yellow]")
            return
        display_matches(results)
    except Exception as e:
        console.print(f"[bold red]Failed to fetch matches: {e}[/bold red]")

# App Main Entry
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context, version: bool = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True)):
    """Main Menu System"""
    f = pyfiglet.figlet_format("Footstats-cli", font="slant")
    print(f)

    if ctx.invoked_subcommand:
        return

    menu_text = Text.assemble(
        "Main Menu\n",
        ("1", "bold cyan"), " - Player Profile\n",
        ("2", "bold cyan"), " - Player Transfer History\n",
        ("3", "bold cyan"), " - Player Stats\n",
        ("4", "bold cyan"), " - Matches\n",
        ("Q", "bold cyan"), " - Quit\n"
    )

    while True:
        try:
            console.print(Panel(menu_text, title="Select an Option"))
            key = readchar.readchar()

            if key == '1':
                name = typer.prompt("Enter player name")
                if not name.strip():
                    console.print("[yellow]Player name cannot be empty.[/yellow]")
                    continue
                player(name=name)

            elif key == '2':
                name = typer.prompt("Enter player name")
                if not name.strip():
                    console.print("[yellow]Player name cannot be empty.[/yellow]")
                    continue
                transfer_history(name=name)

            elif key == '3':
                name = typer.prompt("Enter player name")
                if not name.strip():
                    console.print("[yellow]Player name cannot be empty.[/yellow]")
                    continue
                stats(name=name)

            elif key == '4':
                match_date = typer.prompt(
                    "Enter date (YYYY-MM-DD) or press Enter for today",
                    default=date.today().isoformat()
                )
                matches(match_date=match_date)

            elif key.lower() == 'q':
                console.print("[bold yellow]Exiting...[/bold yellow]")
                break

            else:
                console.print("[bold red]Invalid selection. Try again.[/bold red]")

        except KeyboardInterrupt:
            console.print("\n[bold yellow]Interrupted. Exiting...[/bold yellow]")
            break
        except Exception as e:
            console.print(f"[bold red]Unexpected error: {e}[/bold red]")

    


if __name__ == "__main__":
    app()