import pytest
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from tests.pages.main_page import MainPage
from tests.pages.movie_details_page import MovieDetailsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tests.conftest import logger

@pytest.fixture
def driver():
    logger.info("Starting Chrome WebDriver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://localhost:3000")
    logger.info("Navigated to http://localhost:3000")
    yield driver
    logger.info("Quitting Chrome WebDriver")
    driver.quit()

def test_sort_by_title(driver):
    logger.info("Test: Sort movies by Title and assert last movie is 'The Phantom Menace'")
    main_page = MainPage(driver)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located(main_page.title_header))
    time.sleep(2)  # Wait to visually confirm the click happened
    main_page.get_title_header().click()
    logger.info("Clicked on Title header to sort movies")
    time.sleep(2)  # Wait to visually confirm the click happened
    wait.until(EC.presence_of_element_located(main_page.get_last_row_locator()))
    last_movie_title = main_page.get_last_row().text
    logger.info(f"Last movie title after sort: {last_movie_title}")
    assert last_movie_title == "The Phantom Menace"

def test_view_movie_details_and_check_species(driver):
    logger.info("Test: View 'The Empire Strikes Back' and check if 'Species' list has 'Wookiee'")
    main_page = MainPage(driver)
    movie_details_page = MovieDetailsPage(driver)
    wait = WebDriverWait(driver, 20)
    time.sleep(2)  # Wait to visually confirm the click happened
    wait.until(EC.presence_of_element_located(main_page.get_empire_strikes_back_link_locator()))
    main_page.get_empire_strikes_back_link().click()
    logger.info("Clicked on 'The Empire Strikes Back' movie row")
    wait.until(EC.presence_of_element_located(movie_details_page.get_species_list_locator()))
    species_list = [el.text for el in movie_details_page.get_species_list()]
    logger.info(f"Species list: {species_list}")
    assert any("Wookie" in s for s in species_list)

def test_check_planets_not_in_movie(driver):
    logger.info("Test: Assert that 'Planets' 'Kamino' is not part of the movie 'The Phantom Menace'")
    main_page = MainPage(driver)
    movie_details_page = MovieDetailsPage(driver)
    wait = WebDriverWait(driver, 20)
    time.sleep(2)  # Wait to visually confirm the click happened
    wait.until(EC.presence_of_element_located(main_page.get_phantom_menace_link_locator()))
    main_page.get_phantom_menace_link().click()
    logger.info("Clicked on 'The Phantom Menace' movie row")
    wait.until(EC.presence_of_element_located(movie_details_page.get_planets_list_locator()))
    planets_list = [planet.text for planet in movie_details_page.get_planets_list()]
    logger.info(f"Planets list: {planets_list}")
    assert all("Kamino" not in p for p in planets_list)
