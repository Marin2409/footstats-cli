import typer

# Import functions from the transfermarket provider
from src.providers.transfermarket import (
    get_player_transfer_history,
    get_search_results,
    get_player_profile
)

# Init Typer
app = typer.Typer()

# CLI command to get player profile
@app.command()
def player(name: str):
    players = get_search_results(name)

    if not players:
        print("No players found")
        return
    
    for i, player in enumerate(
        players,
        start=1
    ):
        print(
            f"{i}. {player.name}"
        )

    
    choice = typer.prompt(
        "\nSelect player",
        type=int
    )

    selected = players[choice - 1]

    player_profile = get_player_profile(selected.url)

    print(f"Player profile: {player_profile}")

# CLI command to get player transfer history
@app.command()
def transfer_history(name: str):
    players = get_search_results(name)

    if not players:
        print("No players found")
        return
    
    for i, player in enumerate(
        players,
        start=1
    ):
        print(
            f"{i}. {player.name}"
        )

    
    choice = typer.prompt(
        "\nSelect player",
        type=int
    )

    selected = players[choice - 1]

    transfer_history = get_player_transfer_history(selected.url)
    print(f"Player transfer history: {transfer_history}")

# CLI command to get player stats


if __name__ == "__main__":
    app()