import requests
import time

from bs4 import BeautifulSoup
from src.utils.config import headers as request_headers

# Request to Transfermarkt and test connections
def transfermarkt_request_to_soup(url):
        
        # Sleep for 3 seconds
        time.sleep(3)

        # Make Request
        response = requests.get(
            url,
            headers=request_headers
        )

        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(
                f"Request to {response.url} failed with status code {response.status_code}"
            )
        else:
            print(f"\nRequest to '{url}' successful.")
            print("Status:", response.status_code, "\n")
        
        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        return soup
