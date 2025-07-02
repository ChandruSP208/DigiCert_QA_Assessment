import logging

# Configure logger for API tests
api_logger = logging.getLogger("starwars_api_tests")
api_logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
handler.setFormatter(formatter)
api_logger.addHandler(handler)
