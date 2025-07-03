import pytest
from utils.api_client import ApiClient
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="module")
def api_client():
    return ApiClient()

def test_get_movies_count(api_client):
    logger.info("Testing: Get the list of movies and check if the movies count is 6")
    data = api_client.get("/films/")
    logger.info(f"Response JSON: {data}")
    assert data["count"] == 6

def test_get_third_movie_director(api_client):
    logger.info("Testing: Get the 3rd movie and check if the director is 'Richard Marquand'")
    data = api_client.get("/films/3/")
    director = data.get("fields", {}).get("director")
    logger.info(f"Director: {director}")
    assert director == "Richard Marquand"

def test_get_fifth_movie_producers(api_client):
    logger.info("Testing: Get the 5th movie and assert that 'Producers' are not 'Gary Kurtz, George Lucas'")
    data = api_client.get("/films/5/")
    producer = data.get("fields", {}).get("producer")
    logger.info(f"Producers: {producer}")
    assert producer != "Gary Kurtz, George Lucas"
