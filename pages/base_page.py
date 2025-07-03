from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger(__name__)

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find_element(self, by_locator) -> WebElement:
        logger.info(f"Finding element with locator: {by_locator}")
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def find_elements(self, by_locator) -> list[WebElement]:
        logger.info(f"Finding elements with locator: {by_locator}")
        return self.wait.until(EC.presence_of_all_elements_located(by_locator))

    def click(self, by_locator):
        logger.info(f"Clicking on element with locator: {by_locator}")
        self.find_element(by_locator).click()

    def get_text(self, by_locator) -> str:
        logger.info(f"Getting text from element with locator: {by_locator}")
        return self.find_element(by_locator).text
