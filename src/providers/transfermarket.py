# Package Imports
import re
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Config
from src.utils.config import pattern as player_id_pattern
from src.utils.config import birthday_pattern
from src.utils.config import search_url_template
from src.utils.config import transfer_history_url_template
from src.utils.config import player_stats_url_template
from src.utils.config import base_url

# Database Models
from src.models.player_profile_db import Player
from src.models.player_transfer_history_db import Transfer
from src.models.player_stats_db import StatRow

# Utils
from src.utils.request_to_soup import transfermarkt_request_to_soup
from src.utils.parse import parse_citizenship

# Headers 
request_headers = {
    "User-Agent":      os.getenv("USER_AGENT", "Mozilla/5.0"),
    "Accept-Language": os.getenv("ACCEPT_LANGUAGE", "en-US,en;q=0.5"),
    "Accept-Encoding": os.getenv("ACCEPT_ENCODING", "gzip, deflate"),
}

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
                url=full_url,
            )
        )

    return players

# Get Player Profile
def get_player_profile(player_url: str) -> Player:

    # Make Request and parse with BeautifulSoup
    soup = transfermarkt_request_to_soup(player_url)

    # Extract player ID from URL -------------------------------------
    player_id = get_player_id(player_url)

    # Extract player name --------------------------------------------
    name_tag = soup.find(
        "h1", 
        class_="data-header__headline-wrapper"
    )

    name = "Unknown Player"

    # Extract player name if name tag is found
    if name_tag:

        # Extract first and last names separately
        full_name = name_tag.text.strip()
        parts = full_name.split(' ', 1)  # Split at the first space character
        if len(parts) == 2:  # If there's only one space, it means we have a first and last name
            first_name = parts[0].lower()
            last_name = parts[1].lower()
            name = f"{first_name} {last_name}"

            # Removes any leading # and digits from the name (e.g., "#10lionelmessi" -> "Lionel Messi")
            name = re.sub(r'^#\d+\s*', '', name)
            name = name.title()

    # Extract market value --------------------------------------------
    market_value = None

    # Extract market value from market value tag
    value_tag = soup.find(
        "a",
        class_="data-header__market-value-wrapper"
    )

    # Extract market value if the tag is found
    if value_tag:
        market_value = "".join(
            value_tag.get_text(
                separator=" ",
                strip=True
            )
            .split("Last")[0]
            .split()
        )

    # Extract Age value -----------------------------------------------
    age = None

    # Extract birth date from birth tag
    birth_tag = soup.find(
        "span",
        itemprop="birthDate"
    )
    # Extract age if birth tag is found
    if birth_tag:

        # Extract birth text and clean it up
        birth_text = birth_tag.get_text(
        " ",
        strip=True
        )

        # Use regex to extract age from birth text
        match = re.search(
            birthday_pattern,
            birth_text
        )

        # Extract age if regex match is found
        if match:
            age = int(match.group(1))

    # Extract birthday value ----------------------------------------------
    birthday = None

    if birth_tag:
        birth_text = birth_tag.get_text(
            " ",
            strip=True
        )

        birthday = birth_text.split("(")[0].strip()

    # Extract Club value ----------------------------------------------
    club = None

    # Extract club from club tag
    club_tag = soup.find(
        "span",
        class_="data-header__club"
    )

    # Extract club if club tag is found
    if club_tag:
        club = club_tag.get_text(strip=True)

    # Extract position value ------------------------------------------
    position = None

    # Extract position from position tag
    position_tag = soup.find(
        "dd",
        class_="detail-position__position"
    )

    # Extract position if position tag is found
    if position_tag:
        position = position_tag.get_text(strip=True)

    # Extract Other Positions value -------------------------------------------
    other_positions = None

    # Find the "Other position:" title, then grab all sibling <dd> tags
    other_position_tag = soup.find(
        "dt",
        class_="detail-position__title",
        string=lambda t: t and "Other position:" in t  # type: ignore[call-overload]
    )

    if other_position_tag:
        parent_dl = other_position_tag.find_parent("dl")
        if parent_dl:
            other_position_tags = parent_dl.find_all(
                "dd",
                class_="detail-position__position"
            )
            if other_position_tags:
                other_positions = [
                    dd.get_text(strip=True)
                    for dd in other_position_tags
                ]


    # Extract height value ----------------------------------------------------
    height = None

    # Extract height from height tag
    height_tag = soup.find(
        "span",
        itemprop="height"
    )

    # Extract height if height tag is found
    if height_tag:
        height = height_tag.get_text(strip=True)

    # Extract Place of Birth value --------------------------------------------
    place_of_birth = None

    # Extract place of birth from place of birth tag
    place_of_birth_tag = soup.find(
        "span",
        itemprop="birthPlace"
    )

    # Extract place of birth if tag is found
    if place_of_birth_tag:
        place_of_birth = place_of_birth_tag.get_text(strip=True)

    # Extract Citizenship value --------------------------------------------
    citizenship = None

    citizenship_label = soup.find(  
        "span",
        class_="info-table__content info-table__content--regular",
        string=lambda t: t and "Citizenship:" in t  # type: ignore[call-overload]
    )

    if citizenship_label:
        citizenship_sibling = citizenship_label.find_next_sibling(
            "span",
            class_="info-table__content info-table__content--bold"
        )
        citizenship = parse_citizenship(citizenship_sibling)

    # Extract Foot value --------------------------------------------
    foot = None

    foot_label = soup.find(  
        "span",
        class_="info-table__content info-table__content--regular",
        string=lambda t: t and "Foot:" in t  # type: ignore[call-overload]     
    )

    if foot_label:
        foot_sibling = foot_label.find_next_sibling(
            "span",
            class_="info-table__content info-table__content--bold"
        )
        if foot_sibling:
            foot = foot_sibling.get_text(strip=True)

    # Create and return Player object ---------------------------------
    return Player(
        id=player_id,
        name=name,
        url=player_url,
        market_value=market_value,
        age=age,
        birthday=birthday,
        club=club,
        position=position,
        other_positions=other_positions,
        height=height,
        place_of_birth=place_of_birth,
        citizenship=citizenship,
        foot=foot,
    )

# Get Player transfer history
def get_player_transfer_history(player_url: str) -> list[Transfer]:

    player_id = get_player_id(player_url)

    api_url = transfer_history_url_template.format(player_id=player_id)

    # Use requests directly — this is a JSON API, not an HTML page
    response = requests.get(api_url, headers=request_headers)

    if response.status_code != 200:
        raise Exception(f"Request to {api_url} failed with status {response.status_code}")

    data = response.json()

    transfers = []
    for item in data.get("transfers", []):
        transfers.append(Transfer(
            season=item.get("season"),
            date=item.get("date"),
            left=item.get("from", {}).get("clubName"),
            joined=item.get("to", {}).get("clubName"),
            mv=item.get("marketValue"),
            fee=item.get("fee"),
        ))

    return transfers

# Get Player stats
def get_player_stats(player_url: str) -> list[StatRow]:

    player_id = get_player_id(player_url)

    api_url = player_stats_url_template.format(player_id=player_id)

    response = requests.get(api_url, headers=request_headers)

    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")

    data = response.json()
    performance = data.get("data", {}).get("performance", [])

    stat_rows = []
    for item in performance:
        game_info = item.get("gameInformation", {})
        stats = item.get("statistics", {})
        general = stats.get("generalStatistics", {})
        goals = stats.get("goalStatistics", {})
        cards = stats.get("cardStatistics", {})
        time = stats.get("playingTimeStatistics", {})
        duels = stats.get("duelStatistics", {})
        dist = stats.get("distributionStatistics", {})

        stat_rows.append(StatRow(
            game_id=game_info.get("gameId"),
            season=game_info.get("season", {}).get("nonCyclicalName"),
            competition_id=game_info.get("competitionId"),
            date=game_info.get("date", {}).get("dateTimeUTC"),
            participation=general.get("participationState"),
            minutes_played=time.get("playedMinutes"),
            goals=goals.get("goalsScoredTotal"),
            assists=goals.get("assists"),
            yellow_cards=cards.get("yellowCardNet"),
            red_cards=cards.get("fairPlayPoints"),
            shots=goals.get("scoringAttempts"),
            shots_on_goal=goals.get("scoringAttemptsOnGoal"),
            passes=dist.get("passes"),
            passes_completed=dist.get("passesReached"),
            tackles=duels.get("tackles"),
            fouls_committed=duels.get("foulsCommitted"),
            fouls_gained=duels.get("foulsGained"),
            is_starting=time.get("isStarting"),
            is_captain=general.get("isCaptain"),
        ))

    return stat_rows

