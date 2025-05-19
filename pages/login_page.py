import email

from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage):
    backIcon = (AppiumBy.ACCESSIBILITY_ID, "Back")
    createAccountLink = (AppiumBy.ACCESSIBILITY_ID, "Create account")
    emailInput = (AppiumBy.ACCESSIBILITY_ID, 'Email')
    continueButton = (AppiumBy.ACCESSIBILITY_ID, 'Continue')
    passwordButton = (AppiumBy.ACCESSIBILITY_ID, 'Password')
    logInButton = (AppiumBy.ACCESSIBILITY_ID, 'Log in')


    def go_to_create_account_page(self):
        self.click(*self.createAccountLink)

    def click_continue_button(self):
        self.click(*self.continueButton)

    def go_to_home_page(self):
        self.click(*self.backIcon)

    def click_email_input(self):
        self.click(*self.emailInput)

    def enter_email(self, email):
        self.send_keys(*self.emailInput,email)

    def enter_email_then_continue(self,email):
        self.enter_email(email)
        self.click_continue_button()

    def click_log_in_button(self):
        self.click(*self.logInButton)

    def login(self, email, password):
        self.enter_email_then_continue(email)
        self.enter_password(password)
        self.click_log_in_button()


    def enter_password(self, password):
        self.send_keys(*self.passwordButton, password)


