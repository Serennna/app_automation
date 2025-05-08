import pytest
from utils.driver_manager import create_driver
from utils.logger import log
from pages.home_page import HomePage
from utils.navigations import reset_to_logged_out_home

@pytest.fixture(scope="function")
def driver():
    driver = create_driver()
    yield driver
    reset_to_logged_out_home(driver)
    # driver.quit()

def test_navigate_to_login_page(driver):
    home_page = HomePage(driver)
    home_page.go_to_login_page()
    assert home_page.is_login_page(), "Failed to navigate to the login page"










