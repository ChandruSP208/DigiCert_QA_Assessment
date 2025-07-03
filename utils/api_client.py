import requests
from utils.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)

class ApiClient:
    def __init__(self):
        self.base_url = Config.API_BASE_URL

    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Making GET request to {url}")
        response = requests.get(url, **kwargs)
        logger.info(f"Response status code: {response.status_code}")
        logger.debug(f"Response body: {response.text}")
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
