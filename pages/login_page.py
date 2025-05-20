import email
import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage):
    BACK_ICON = (AppiumBy.ACCESSIBILITY_ID, "Back")
    CREATE_ACCOUNT = (AppiumBy.ACCESSIBILITY_ID, "Create account")
    EMAIL_INPUT = (AppiumBy.ACCESSIBILITY_ID, 'Email')
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Continue')
    PASSWORD_INPUT = (AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')
    PASSWORD = (AppiumBy.ACCESSIBILITY_ID, 'Password')
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Log in')
    ALARM_ICON = (AppiumBy.CLASS_NAME, "XCUIElementTypeImage")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_create_account_page(self):
        self.click(*self.CREATE_ACCOUNT)

    def go_to_home_page(self):
        self.click(*self.BACK_ICON)

    def click_email_input(self):
        self.click(*self.EMAIL_INPUT)

    def enter_email(self, email):
        self.send_keys(*self.EMAIL_INPUT,email)

    def enter_email_then_continue(self,email):
        self.click(*self.EMAIL_INPUT)
        self.enter_email(email)
        self.click(*self.CONTINUE_BUTTON)

    def click_log_in_button(self):
        self.click(*self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email_then_continue(email)
        if self.is_displayed(*self.ALARM_ICON):
            self.click(*self.CONTINUE_BUTTON)
        time.sleep(5)
        self.enter_password(password)
        time.sleep(2)
        self.click(*self.LOGIN_BUTTON)

    def enter_password(self, password):
        self.click(*self.PASSWORD)
        self.find(*self.PASSWORD_INPUT).clear().send_keys(password)

    def is_login_required(self):
        """检查当前是否需要登录"""
        return self.is_displayed(self.LOGIN_BUTTON)
