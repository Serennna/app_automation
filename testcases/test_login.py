import pytest
from utils.driver_manager import create_driver
from utils.logger import log
from pages.home_page import HomePage

@pytest.fixture(scope="function")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

def test_login_success(driver):
    login_page = HomePage(driver)
    login_page.login("testuser", "123456")

