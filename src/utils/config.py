# TransferMarket .config 
# -----------------------------------------------------------------------------------------

# Regex pattern to extract player ID from URL
pattern = r"/profil/spieler/(\d+)"

# Regex pattern to extract player birthday from profile page
birthday_pattern = r"\((\d+)\)"

# Base URL for Transfermarkt 
TFbase_url = "https://www.transfermarkt.com"

# Search Player profile URL
search_url_template = f"{TFbase_url}/schnellsuche/ergebnis/schnellsuche?query={{name}}"

# Transfer history URL template
transfer_history_url_template = f"{TFbase_url}/ceapi/transferHistory/list/{{player_id}}"

# Player Stats URL template
player_stats_url_template = f"https://tmapi-alpha.transfermarkt.technology/player/{{player_id}}/performance-game"

# -----------------------------------------------------------------------------------------

# FBref Soccer .config 
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------