from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.title_header = (By.XPATH, "//th[contains(text(), 'Title')]")
        self.last_row = (By.XPATH, "//tbody/tr[last()]/td[1]")
        self.empire_strikes_back_link = (By.XPATH, "//td/a[contains(text(), 'The Empire Strikes Back')]")
        self.phantom_menace_link = (By.XPATH, "//td/a[contains(text(), 'The Phantom Menace')]")

    def sort_by_title(self):
        self.click(self.title_header)

    def get_last_movie_title(self) -> str:
        return self.get_text(self.last_row)

    def click_movie_link(self, movie_title: str):
        locator = (By.XPATH, f"//td/a[contains(text(), '{movie_title}')]")
        self.click(locator)
