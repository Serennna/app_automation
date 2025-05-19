from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from appium.webdriver.common.appiumby import AppiumBy

class Marketplace(BasePage):
    profileIcon = (AppiumBy.CLASS_NAME, "XCUIElementTypeImage")
    marketplaceTab = (AppiumBy.XPATH,'''//XCUIElementTypeButton[@name="Marketplace"]''')

    def is_logged_in(self):
        ''' check log-in status '''
        try:
            self.find(*self.profileIcon,index=1)
            return True
        except:
            return False

    def enter_marketplace_with_login_check(self, email, password):
        ''' make sure user logged in already '''
        if not self.is_logged_in():
            # back to home paeg
            home_page = HomePage(self.driver)
            home_page.go_to_login_page()

            # login
            login_page = LoginPage(self.driver)
            login_page.login(email, password)
        return self

