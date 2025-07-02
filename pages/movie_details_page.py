from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import logging

from tests.conftest import logger

class MovieDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.back_button = (By.XPATH, "//a[contains(text(), 'Back')]")
        self.species_list = (By.XPATH, "//h1[text()='Species']/following::ul[1]/li")
        self.planets_list = (By.XPATH, "//h1[text()='Planets']/following::ul[1]/li")
    def get_species_list_locator(self):
        return self.species_list

    def get_planets_list_locator(self):
        return self.planets_list

    def get_back_button(self) -> WebElement:
        logger.info("Locating Back button on details page")
        return self.driver.find_element(*self.back_button)

    def get_species_list(self) -> list[WebElement]:
        logger.info("Getting species list from details page")
        return self.driver.find_elements(*self.species_list)

    def get_planets_list(self) -> list[WebElement]:
        logger.info("Getting planets list from details page")
        return self.driver.find_elements(*self.planets_list)
