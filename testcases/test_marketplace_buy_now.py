# tests/test_marketplace_buy_now.py
import allure
from utils.navigations import reset_to_marketplace
from data.test_data import TestUser
from utils.driver_manager import DriverManager
import pytest

@pytest.fixture(scope="function")
def driver(setup_driver):
    yield setup_driver
    reset_to_marketplace(setup_driver)
    # setup_driver.quit()

@allure.epic("Marketplace")
@allure.feature("Buy Now")
class TestMarketplaceBuyNow:


    @allure.story("用户登录后导航到 Marketplace")
    @allure.severity(allure.severity_level.NORMAL)
    def test_successful_login_then_navigate_to_marketplace(self, login_page, marketplace_page):
        """测试登录后成功跳转到Marketplace页面"""
        # 登录操作
        login_page.login(*TestUser)

        # 导航到Marketplace
        marketplace_page.navigate_to_marketplace()

        # 验证是否在Marketplace页面
        assert marketplace_page.is_marketplace_tab_active(), "Marketplace tab should be active"

        # 验证Marketplace页面元素
        assert marketplace_page.is_displayed(marketplace_page.SEARCH_BAR), "Search bar should be visible"
