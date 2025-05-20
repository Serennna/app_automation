from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class HomePage(BasePage):
    createAccountButton = (AppiumBy.ACCESSIBILITY_ID, "Create account")
    loginButton = (AppiumBy.ACCESSIBILITY_ID, 'Log in')
    browseTheAppButton = (AppiumBy.ACCESSIBILITY_ID, 'Browse the app')

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_create_account_page(self):
        self.click(*self.createAccountButton)

    def go_to_login_page(self):
        self.click(*self.loginButton)

    def guest_mode(self):
        self.click(*self.browseTheAppButton)

    def is_on_logged_out_home(self):
        try:
            return (
                self.driver.find_element(*self.createAccountButton).is_displayed() and
                self.driver.find_element(*self.loginButton).is_displayed() and
                self.driver.find_element(*self.browseTheAppButton).is_displayed()
            )
        except Exception:
            return False

    def is_login_page(self):
        try:
            return self.driver.find_element((AppiumBy.ACCESSIBILITY_ID,'Email')).is_displayed()
        except Exception:
            return False