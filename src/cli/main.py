import typer

from src.providers.transfermarket import (
    get_search_results
)

app = typer.Typer()


@app.command()
def player(name: str):
    players = get_search_results(name)

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

    print(f"\nSelected player: {selected}")


if __name__ == "__main__":
    app()