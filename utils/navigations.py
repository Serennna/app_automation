from data.test_data import TestUser
from pages.home_page import HomePage
from pages.marketplace_page import MarketplacePage


def reset_to_logged_out_home(driver):
    home = HomePage(driver)  # 传递 driver 参数
    if home.is_on_logged_out_home():
        return
    try:
        for _ in range(3):
            driver.back()
            if home.is_on_logged_out_home():
                return
        driver.close_app()
        driver.launch_app()
        assert home.is_on_logged_out_home()
    except Exception as e:
        print(f"Failed to reset to logged out home: {e}")


def reset_to_marketplace(driver):
    marketplace_page = MarketplacePage(driver)
    marketplace_page.ensure_marketplace_with_login_check(*TestUser)


