from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MovieDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.back_button = (By.XPATH, "//a[contains(text(), 'Back')]")
        self.species_list = (By.XPATH, "//h1[text()='Species']/following::ul[1]/li")
        self.planets_list = (By.XPATH, "//h1[text()='Planets']/following::ul[1]/li")

    def get_species(self) -> list[str]:
        elements = self.find_elements(self.species_list)
        return [element.text for element in elements]

    def get_planets(self) -> list[str]:
        elements = self.find_elements(self.planets_list)
        return [element.text for element in elements]

    def go_back(self):
        self.click(self.back_button)
