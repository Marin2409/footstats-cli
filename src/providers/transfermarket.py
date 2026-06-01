import re
import requests
import time

from bs4 import BeautifulSoup
from src.config import pattern as player_id_pattern
from src.config import headers as request_headers
from src.models.player_db import Player

# Request to Transfermarkt and test connections
def transfermarkt_request_to_soup(url):
        time.sleep(3)
        response = requests.get(
            url,
            headers=request_headers
        )

        print("\nStatus:", response.status_code)
        print("URL:", response.url, "\n")

        soup = BeautifulSoup(response.content, 'html.parser')

        return soup

# Extract player ID from URL
def get_player_id(player_url):
    match = re.search(
        player_id_pattern,
        player_url
    )

    if not match:
        raise ValueError(
            f"Could not extract player ID from {player_url}"
        )

    return match.group(1)

# Get search results for a player name
def get_search_results(name):
    search_url = (
        f"https://www.transfermarkt.com/"
        f"schnellsuche/ergebnis/schnellsuche?query={name}"
    )

    soup = transfermarkt_request_to_soup(search_url)

    players = []

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if "/profil/spieler/" not in href:
            continue

        player_name = link.get_text(strip=True)

        if not player_name:
            continue

        full_url = f"https://www.transfermarkt.com{href}"

        players.append(
            Player(
                id=get_player_id(full_url),
                name=player_name,
                url=full_url
            )
        )

    return players