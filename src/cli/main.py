import typer
import readchar
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


from src.providers.transfermarket import (
    get_player_transfer_history,
    get_player_profile,
    get_player_stats,
)

from src.cli.utils.utils import (
    display_player_profile, 
    display_transfer_history,
    display_stats,
    select_player,
    version_callback
)

app = typer.Typer(rich_markup_mode="rich")
console = Console()

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

@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context, 
    version: bool = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True)
    ):
    """Main Menu System"""
    if ctx.invoked_subcommand:
        return

    menu_text = Text.assemble(
        "Main Menu\n",
        ("1", "bold cyan"), " - Player Profile\n",
        ("2", "bold cyan"), " - Player Transfer History\n",
        ("3", "bold cyan"), " - Player Stats\n",
        ("Q", "bold cyan"), " - Quit\n"
    )

    while True:
        try:
            console.print(Panel(menu_text, title="Select an Option"))
            key = readchar.readchar()

            if key in ('1', '2', '3'):
                name = typer.prompt("Enter player name")
                if not name.strip():
                    console.print("[yellow]Player name cannot be empty.[/yellow]")
                    continue
                if key == '1':
                    player(name=name)
                elif key == '2':
                    transfer_history(name=name)
                elif key == '3':
                    stats(name=name)
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