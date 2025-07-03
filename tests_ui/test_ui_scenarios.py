import time
from pages.main_page import MainPage
from pages.movie_details_page import MovieDetailsPage
from utils.logger import get_logger

logger = get_logger(__name__, 'ui_automation.log')

def test_sort_by_title(driver):
    logger.info("Test: Sort movies by Title and assert last movie is 'The Phantom Menace'")
    main_page = MainPage(driver)
    time.sleep(2) # Added for visibility
    main_page.sort_by_title()
    time.sleep(2) # Added for visibility
    last_movie_title = main_page.get_last_movie_title()
    logger.info(f"Last movie title after sort: {last_movie_title}")
    assert last_movie_title == "The Phantom Menace"

def test_view_movie_details_and_check_species(driver):
    logger.info("Test: View 'The Empire Strikes Back' and check if 'Species' list has 'Wookiee'")
    main_page = MainPage(driver)
    movie_details_page = MovieDetailsPage(driver)
    time.sleep(2) # Added for visibility
    main_page.click_movie_link("The Empire Strikes Back")
    species_list = movie_details_page.get_species()
    time.sleep(5)
    logger.info(f"Species list: {species_list}")
    assert any("Wookie" in s for s in species_list)
    movie_details_page.go_back()

def test_check_planets_not_in_movie(driver):
    logger.info("Test: Assert that 'Planets' 'Kamino' is not part of the movie 'The Phantom Menace'")
    main_page = MainPage(driver)
    movie_details_page = MovieDetailsPage(driver)
    time.sleep(2) # Added for visibility
    main_page.click_movie_link("The Phantom Menace")
    planets_list = movie_details_page.get_planets()
    time.sleep(5)
    logger.info(f"Planets list: {planets_list}")
    assert "Kamino" not in planets_list
    movie_details_page.go_back()
