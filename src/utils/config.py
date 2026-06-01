# Configuration file for the scraper
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
}

# Regular expression pattern to extract player ID from URL
pattern = r"/profil/spieler/(\d+)"

# Base URL for Transfermarkt 
base_url = "https://www.transfermarkt.com"

# Search Player profile URL
search_url_template = f"{base_url}/schnellsuche/ergebnis/schnellsuche?query={{name}}"