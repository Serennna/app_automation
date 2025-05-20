import pytest
from appium import webdriver

from data.test_data import TestUser
from pages.marketplace_page import MarketplacePage
from utils.driver_manager import DriverManager
from utils.logger import setup_logger
import datetime
import os
from utils.constants import REPORT_DIR


@pytest.fixture(scope="function")
def setup_driver():
    """初始化Appium driver"""
    driver = None
    try:
        driver = DriverManager.get_driver()
        yield driver
    finally:
        if driver:
            driver.quit()

# conftest.py
@pytest.fixture
def login_page(driver):
    from pages.login_page import LoginPage
    return LoginPage(driver)

@pytest.fixture
def home_page(driver):
    from pages.home_page import HomePage
    return HomePage(driver)

@pytest.fixture
def marketplace_page(driver):
    from pages.marketplace_page import MarketplacePage
    return MarketplacePage(driver)


@pytest.fixture(scope="function")
def marketplace(driver, request, marketplace_page):
    """Marketplace模块的fixture，自动处理登录状态和tab恢复"""
    logger = setup_logger("marketplace_fixture")

    # 1. 检查登录状态
    from pages.login_page import LoginPage
    login_page = LoginPage(driver)
    if login_page.is_login_required():  # 需要在LoginPage中实现这个方法
        logger.info("User not logged in, performing login...")
        home_page = login_page.login(*TestUser)
    # 2. 导航到Marketplace
    marketplace_page = MarketplacePage(driver).navigate_to_marketplace()

    yield marketplace_page

    # 3. Teardown: 确保测试结束后回到Marketplace tab
    logger.info("Tearing down - returning to Marketplace tab")
    try:
        marketplace_page.navigate_to_marketplace()
    except Exception as e:
        logger.error(f"Failed to return to Marketplace tab: {str(e)}")
        take_screenshot(driver, "teardown_failure")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 获取测试结果
    outcome = yield
    rep = outcome.get_result()

    # 设置报告属性
    setattr(item, "rep_" + rep.when, rep)


def take_screenshot(driver, test_name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = os.path.join(REPORT_DIR, "screenshots")
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path


# 添加自定义断言日志
def pytest_assertrepr_compare(op, left, right):
    logger = setup_logger("assert")
    logger.info(f"Assertion: {left} {op} {right}")

    if isinstance(left, str) and isinstance(right, str):
        return [
            f"Comparison: {left} {op} {right}",
            f"Details:",
            f"  Left: {left}",
            f"  Right: {right}"
        ]