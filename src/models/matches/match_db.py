from dataclasses import dataclass
from typing import Optional

@dataclass
class Match:
    competition: Optional[str]
    round: Optional[str]
    date: Optional[str]
    home: Optional[str]
    score: Optional[str]
    away: Optional[str]
    venue: Optional[str]