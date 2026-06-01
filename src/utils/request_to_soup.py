import requests
import time

from bs4 import BeautifulSoup
from src.utils.config import headers as request_headers

# Request to Transfermarkt and test connections
def transfermarkt_request_to_soup(url):
        time.sleep(3)
        response = requests.get(
            url,
            headers=request_headers
        )

        # Debugging information
        print("\nStatus:", response.status_code)
        print("URL:", response.url, "\n")

        soup = BeautifulSoup(response.content, 'html.parser')

        return soup
