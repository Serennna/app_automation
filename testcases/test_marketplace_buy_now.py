# tests/test_marketplace_buy_now.py
import allure
from utils.navigations import reset_to_marketplace
from data.test_data import TestUser, TestAppName
from utils.driver_manager import DriverManager
import pytest

@pytest.fixture(scope="function")
def driver(setup_driver):
    yield setup_driver
    setup_driver.terminate_app(TestAppName)
    # setup_driver.quit()

@allure.epic("Marketplace")
@allure.feature("Buy Now")
class TestMarketplaceBuyNow:


    @allure.story("Check Marketplace UI")
    @allure.severity(allure.severity_level.NORMAL)
    def test_marketplace_ui(self, login_page, marketplace_page):
        assert marketplace_page.is_marketplace_tab_active(), "Marketplace tab should be active"
        assert marketplace_page.is_displayed(marketplace_page.SEARCH_BAR), "Search bar should be visible"

    @allure.story("Checkout V1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_v1(self, login_page, marketplace_page,pdp, checkout_page):

        # Step1 - Navigating to the first item PDP
        marketplace_page.find(*marketplace_page.CARD_IMAGE).click()

        # Step2 - Clikc Buy Now
        pdp.click(*pdp.BUY_NOW)
        assert checkout_page.is_enabled(*checkout_page.SLIDE_TO_PAY)

        # Step3 - Slide to Pay
        checkout_page.slide_to_pay()

        assert checkout_page.is_displayed(*checkout_page.ORDER_PLACED)
        assert checkout_page.is_displayed(*checkout_page.SHIP_TO_VAULT)
        assert checkout_page.is_enabled(*checkout_page.DONE_BUTTON)
        assert checkout_page.is_displayed(*checkout_page.COMPLETE_LABEL)








