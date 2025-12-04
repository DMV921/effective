import pytest
BASE_URL = "https://effective-mobile.ru"
@pytest.fixture(scope="session")
def base_url():
    return BASE_URL
