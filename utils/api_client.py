import requests
import json
from utils.config import Config
from utils.logger import get_logger

logger = get_logger(__name__, 'api_responses.log')

class ApiClient:
    def __init__(self):
        self.base_url = Config.API_BASE_URL

    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Making GET request to {url}")
        response = requests.get(url, **kwargs)
        logger.info(f"Response status code: {response.status_code}")
        
        try:
            response_json = response.json()
            # Log the full response to the file at DEBUG level
            logger.debug(f"Full API Response from {url}:\n{json.dumps(response_json, indent=2)}")
        except json.JSONDecodeError:
            logger.error(f"Failed to decode JSON from response: {response.text}")
            response_json = None

        response.raise_for_status()  # Raise an exception for bad status codes
        return response_json
