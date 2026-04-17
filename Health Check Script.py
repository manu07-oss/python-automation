import requests
import time
import logging

logging.basicConfig(level=logging.INFO)

def health_check(url, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                logging.info(f"{url} is UP")
                return True
            else:
                logging.warning(f"{url} returned {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error: {e}")
        
        time.sleep(2)

    logging.critical(f"{url} is DOWN after retries")
    return False
