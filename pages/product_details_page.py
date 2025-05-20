from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class PPD(BasePage):

    BUY_NOW = (AppiumBy.ACCESSIBILITY_ID,'Buy now')

    def __init__(self, driver):
        super().__init__(driver)

    def buy_now(self):
        self.click(*self.BUY_NOW)

