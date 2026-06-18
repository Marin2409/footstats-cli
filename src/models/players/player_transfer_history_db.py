from dataclasses import dataclass

@dataclass
class Transfer:
    season: str | None
    date: str | None
    left: str | None
    joined: str | None
    mv: str | None
    fee: str | None