# Headers to mimic a real browser
headers = {
    "User-Agent": 
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36",
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate'
}

# Regex pattern to extract player ID from URL
pattern = r"/profil/spieler/(\d+)"

# Regex pattern to extract player birthday from profile page
birthday_pattern = r"\((\d+)\)"

# Base URL for Transfermarkt 
base_url = "https://www.transfermarkt.com"

# Search Player profile URL
search_url_template = f"{base_url}/schnellsuche/ergebnis/schnellsuche?query={{name}}"

# Transfer history URL template
transfer_history_url_template = f"{base_url}/ceapi/transferHistory/list/{{player_id}}"

# Player Stats URL template
player_stats_url_template = f"{base_url}/{{player_name}}/leistungsdatendetails/spieler/{{player_id}}/saison//verein/0/liga/0/wettbewerb//pos/0/trainer_id/0/plus/1"