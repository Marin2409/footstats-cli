import typer
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

from src.providers.transfermarket import (
    get_search_results
)

def display_player_list(players):
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("#", style="bold cyan", width=4)
    table.add_column("Name", style="white")

    for i, p in enumerate(players, start=1):
        table.add_row(str(i), p.name)

    console.print(table)

def display_player_profile(profile):
    table = Table(box=box.ROUNDED, show_header=False, title=f"[bold]{profile.name}[/bold]")
    table.add_column("Field", style="bold cyan", width=20)
    table.add_column("Value", style="white")

    rows = [
        ("Club",            profile.club or "—"),
        ("Position",        profile.position or "—"),
        ("Other Positions", ", ".join(profile.other_positions) if profile.other_positions else "—"),
        ("Market Value",    profile.market_value or "—"),
        ("Age",             str(profile.age) if profile.age else "—"),
        ("Birthday",        profile.birthday or "—"),
        ("Height",          profile.height or "—"),
        ("Place of Birth",  profile.place_of_birth or "—"),
        ("Citizenship",     profile.citizenship or "—"),
        ("Foot",            profile.foot or "—"),
    ]

    for field, value in rows:
        table.add_row(field, value)

    console.print(table)

def display_transfer_history(transfers):
    table = Table(box=box.ROUNDED, title="Transfer History")
    table.add_column("Season",  style="bold cyan",  no_wrap=True)
    table.add_column("Date",    style="white",       no_wrap=True)
    table.add_column("Left",    style="red")
    table.add_column("Joined",  style="green")
    table.add_column("MV",      style="yellow")
    table.add_column("Fee",     style="magenta")

    for t in transfers:
        table.add_row(
            t.season or "—",
            t.date or "—",
            t.left or "—",
            t.joined or "—",
            t.mv or "—",
            t.fee or "—",
        )

    console.print(table)

def display_stats(stat_rows):
    table = Table(box=box.ROUNDED, title="Player Stats")
    table.add_column("Date",        style="bold cyan",  no_wrap=True)
    table.add_column("Season",      style="white",      no_wrap=True)
    table.add_column("Competition", style="yellow")
    table.add_column("Status",      style="white")
    table.add_column("Mins",        style="white",  justify="right")
    table.add_column("G",           style="green",  justify="right")
    table.add_column("A",           style="blue",   justify="right")
    table.add_column("Y",           style="yellow", justify="right")
    table.add_column("R",           style="red",    justify="right")
    table.add_column("Shots",       style="white",  justify="right")
    table.add_column("Passes",      style="white",  justify="right")

    for r in stat_rows:
        table.add_row(
            (r.date or "—")[:10],
            r.season or "—",
            r.competition_id or "—",
            r.participation or "—",
            str(r.minutes_played) if r.minutes_played is not None else "—",
            str(r.goals)          if r.goals          is not None else "—",
            str(r.assists)        if r.assists         is not None else "—",
            str(r.yellow_cards)   if r.yellow_cards    is not None else "—",
            str(r.red_cards)      if r.red_cards       is not None else "—",
            str(r.shots)          if r.shots           is not None else "—",
            str(r.passes)         if r.passes          is not None else "—",
        )

    console.print(table)

def select_player(name: str):
    try:
        players = get_search_results(name)
    except Exception as e:
        console.print(f"[bold red]Search failed: {e}[/bold red]")
        return None

    if not players:
        console.print("[bold red]No players found.[/bold red]")
        return None

    display_player_list(players)

    try:
        choice = typer.prompt("\nSelect player", type=int)
        return players[choice - 1]
    except (IndexError, ValueError):
        console.print("[bold red]Invalid selection.[/bold red]")
        return None

def version_callback(value: bool):
    if value:
        console.print("[bold cyan]footstats v1.0.0[/bold cyan]")
        raise typer.Exit()