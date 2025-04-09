from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class HomePage(BasePage):
    createAccountButton = (AppiumBy.ACCESSIBILITY_ID, "Create account")
    loginButton = (AppiumBy.ACCESSIBILITY_ID, 'Log in')
    browseTheAppButton = (AppiumBy.ACCESSIBILITY_ID, 'Browse the app')

    def go_to_create_account_page(self):
        self.click(*self.createAccountButton)

    def go_to_login_page(self):
        self.click(*self.loginButton)

    def guest_mode(self):
        self.click(*self.browseTheAppButton)

