import requests
import time
import os

from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

REQUEST_DELAY = float(os.getenv("REQUEST_DELAY", "1.5"))

request_headers = {
    "User-Agent":      os.getenv("USER_AGENT", "Mozilla/5.0"),
    "Accept-Language": os.getenv("ACCEPT_LANGUAGE", "en-US,en;q=0.5"),
    "Accept-Encoding": os.getenv("ACCEPT_ENCODING", "gzip, deflate"),
}

# Request to Transfermarkt and test connections
def transfermarkt_request_to_soup(url):
        
        # Sleep for 3 seconds
        time.sleep(REQUEST_DELAY)

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
        # UNCOMMENT FOR DEBUGGING
        # else:
        #     print(f"\nRequest to '{url}' successful.")
        #     print("Status:", response.status_code, "\n")
        
        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        return soup
