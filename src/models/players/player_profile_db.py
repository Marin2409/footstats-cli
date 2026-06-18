from dataclasses import dataclass

@dataclass
class Player:
    id: str
    name: str
    url: str

    market_value: str | None = None
    age: int | None = None
    birthday: str | None = None
    club: str | None = None
    position: str | None = None
    other_positions: list[str] | None = None
    height: str | None = None
    place_of_birth: str | None = None
    citizenship: str | None = None
    foot: str | None = None

