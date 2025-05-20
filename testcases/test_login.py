# testcases/test_login.py
import allure
from data.test_data import TestUser, TestAppName
from utils.driver_manager import DriverManager
import pytest

from utils.navigations import reset_to_logged_out_home


@pytest.fixture(scope="function")
def driver(setup_driver):
    yield setup_driver
    # reset_to_logged_out_home(setup_driver)
    setup_driver.terminate_app(TestAppName)

@allure.epic("Home Page")
@allure.feature("log in")
class TestLoginPage:

    @allure.story("User Login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_successfully_log_in(self,home_page, login_page,marketplace_page):
        home_page.go_to_login_page()
        print(*TestUser)
        login_page.login(*TestUser)
        # Should be in marketplace page
        assert marketplace_page.is_marketplace_tab_active(), "Marketplace tab should be active"
        assert marketplace_page.is_displayed(marketplace_page.SEARCH_BAR), "Search bar should be visible"
