import re

from src.utils.config import pattern as player_id_pattern
from src.utils.config import search_url_template
from src.utils.config import base_url
from src.models.player_db import Player
from src.utils.request_to_soup import transfermarkt_request_to_soup

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
    search_url = search_url_template.format(name=name)

    soup = transfermarkt_request_to_soup(search_url)

    players = []

    for link in soup.find_all("a", href=True):
        href = link["href"]

        if "/profil/spieler/" not in href:
            continue

        player_name = link.get_text(strip=True)

        if not player_name:
            continue

        full_url = f"{base_url}{href}"

        players.append(
            Player(
                id=get_player_id(full_url),
                name=player_name,
                url=full_url
            )
        )

    return players