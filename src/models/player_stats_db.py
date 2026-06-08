from dataclasses import dataclass
from typing import Optional

@dataclass
class StatRow:
    game_id: Optional[str] = None
    season: Optional[str] = None
    competition_id: Optional[str] = None
    date: Optional[str] = None
    participation: Optional[str] = None
    minutes_played: Optional[int] = None
    goals: Optional[int] = None
    assists: Optional[int] = None
    yellow_cards: Optional[int] = None
    red_cards: Optional[int] = None
    shots: Optional[int] = None
    shots_on_goal: Optional[int] = None
    passes: Optional[int] = None
    passes_completed: Optional[int] = None
    tackles: Optional[int] = None
    fouls_committed: Optional[int] = None
    fouls_gained: Optional[int] = None
    is_starting: Optional[bool] = None
    is_captain: Optional[bool] = None