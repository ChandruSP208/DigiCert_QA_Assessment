import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="session")
def driver():
    logger.info("Setting up Chrome WebDriver.")
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(Config.BASE_URL)
    driver.maximize_window()
    yield driver
    logger.info("Tearing down Chrome WebDriver.")
    driver.quit()
