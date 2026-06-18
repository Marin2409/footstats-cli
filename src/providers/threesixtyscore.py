# Package Imports
# import re
import requests
# import os
# from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import date

load_dotenv()

# Config
# from src.utils.config import TFbase_url

# Database Models
from src.models.matches.match_db import Match

# Utils
# from src.utils.request_to_soup import transfermarkt_request_to_soup

# Headers 
# request_headers = {
#     "User-Agent":      os.getenv("USER_AGENT", "Mozilla/5.0"),
#     "Accept-Language": os.getenv("ACCEPT_LANGUAGE", "en-US,en;q=0.5"),
#     "Accept-Encoding": os.getenv("ACCEPT_ENCODING", "gzip, deflate"),
# }

def get_matches(match_date: date) -> list[Match]:
    url = f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{match_date.isoformat()}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/136.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Origin": "https://www.sofascore.com",
        "Referer": "https://www.sofascore.com/",
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Request to {url} failed with status code {response.status_code}")

    data = response.json()
    events = data.get("events", [])

    matches = []
    for event in events:
        home = event.get("homeTeam", {}).get("name")
        away = event.get("awayTeam", {}).get("name")

        if not home or not away:
            continue

        home_score = event.get("homeScore", {}).get("current")
        away_score = event.get("awayScore", {}).get("current")
        score = f"{home_score} - {away_score}" if home_score is not None and away_score is not None else None

        competition = event.get("tournament", {}).get("name")
        category = event.get("tournament", {}).get("category", {}).get("name")
        if category:
            competition = f"{category} - {competition}"

        venue = event.get("venue", {}).get("name") if event.get("venue") else None

        round_info = event.get("roundInfo", {})
        round_name = round_info.get("name") or (f"Round {round_info.get('round')}" if round_info.get("round") else None)

        matches.append(Match(
            competition=competition,
            round=round_name,
            date=match_date.isoformat(),
            home=home,
            score=score,
            away=away,
            venue=venue,
        ))

    return matches
