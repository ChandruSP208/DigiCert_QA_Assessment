import pytest
import requests
from tests.api_logger import api_logger

BASE_URL = "https://swapi-node.vercel.app/api"

def test_get_movies_count():
    api_logger.info("Testing: Get the list of movies and check if the movies count is 6")
    response = requests.get(f"{BASE_URL}/films/")
    api_logger.info(f"Status code: {response.status_code}")
    api_logger.info(f"Response JSON: {response.json()}")
    assert response.status_code == 200
    assert response.json()["count"] == 6

def test_get_third_movie_director():
    api_logger.info("Testing: Get the 3rd movie and check if the director is 'Richard Marquand'")
    response = requests.get(f"{BASE_URL}/films/3")
    api_logger.info(f"Status code: {response.status_code}")
    data = response.json()
    # The actual film data is under the 'fields' key
    director = data.get("fields", {}).get("director")
    api_logger.info(f"Director: {director}")
    assert director == "Richard Marquand"

def test_get_fifth_movie_producers():
    api_logger.info("Testing: Get the 5th movie and assert that 'Producers' are not 'Gary Kurtz, George Lucas'")
    response = requests.get(f"{BASE_URL}/films/5/")
    api_logger.info(f"Status code: {response.status_code}")
    data = response.json()
    producer = data.get("fields", {}).get("producer")
    api_logger.info(f"Producers: {producer}")
    assert response.status_code == 200
    assert producer != "Gary Kurtz, George Lucas"
