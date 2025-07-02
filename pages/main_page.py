from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import logging

from tests.conftest import logger

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.title_header = (By.XPATH, "//th[contains(text(), 'Title')]")
        self.last_row = (By.XPATH, "//tbody/tr[last()]/td[1]")
        self.empire_strikes_back_link = (By.XPATH, "//td/a[contains(text(), 'The Empire Strikes Back')]")
        self.phantom_menace_link = (By.XPATH, "//td/a[contains(text(), 'The Phantom Menace')]")
    def get_empire_strikes_back_link(self) -> WebElement:
        logger.info("Locating 'The Empire Strikes Back' link")
        return self.driver.find_element(*self.empire_strikes_back_link)

    def get_empire_strikes_back_link_locator(self):
        return self.empire_strikes_back_link

    def get_phantom_menace_link(self) -> WebElement:
        logger.info("Locating 'The Phantom Menace' link")
        return self.driver.find_element(*self.phantom_menace_link)

    def get_phantom_menace_link_locator(self):
        return self.phantom_menace_link

    def get_title_header(self) -> WebElement:
        logger.info("Locating Title header for sorting")
        return self.driver.find_element(*self.title_header)

    # Returns locator tuple for last row, for use in waits
    def get_last_row_locator(self):
        return self.last_row

    # Returns WebElement for last row
    def get_last_row(self) -> WebElement:
        logger.info("Locating the last movie row")
        return self.driver.find_element(*self.last_row)

    def get_movie_by_title(self, title: str) -> WebElement:
        logger.info(f"Locating movie row by title: {title}")
        return self.driver.find_element(By.XPATH, f"//td[contains(text(), '{title}')]")
