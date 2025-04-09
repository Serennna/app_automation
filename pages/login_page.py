from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class LoginPage(BasePage):
    backIcon = (AppiumBy.ACCESSIBILITY_ID, "Back")
    createAccountLink = (AppiumBy.ACCESSIBILITY_ID, "Create account")
    emailInput = (AppiumBy.ACCESSIBILITY_ID, 'Email')
    continueButton = (AppiumBy.ACCESSIBILITY_ID, 'Continue')
    passwordButton = (AppiumBy.ACCESSIBILITY_ID, 'Password')


    def go_to_create_account_page(self):
        self.click(*self.createAccountLink)

    def click_continue_button(self):
        self.click(*self.continueButton)

    def go_to_home_page(self):
        self.click(*self.backIcon)

    def click_email_input(self):
        self.click(*self.emailInput)

    def enter_email(self, email):
        self.click(*self.emailInput)
        self.send_keys(email)

    def enter_email_then_continue(self,email):
        self.enter_email(email)
        self.click_continue_button()

    def checkEmailLabel(self, checkValue):
        """when user enters email then continue, check the email label displays correctly"""
        emailLabel = self.get_text(AppiumBy.ACCESSIBILITY_ID, checkValue)
        emailLabel
