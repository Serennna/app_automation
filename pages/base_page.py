from appium.webdriver.webdriver import WebDriver
from data.app_params import *
from typing import NoReturn
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    BackArrow = (AppiumBy.ACCESSIBILITY_ID, 'Back')


    def __init__(self, driver: WebDriver):
        self.driver = driver

    '''App activity'''

    # def open_app(self) -> NoReturn:
    #     if device_type == 'Real':
    #         self.driver.activate_app(get_app_name('Dev'))
    #     else:
    #         self.driver.activate_app(app_name)
    #
    # def close_app(self) -> NoReturn:
    #     if device_type == 'Real':
    #         self.driver.terminate_app(get_app_name('Dev'))
    #     else:
    #         self.driver.terminate_app(app_name)

    def find(self, locator_type, value):
        return self.driver.find_element(locator_type, value)

    def click(self, locator_type, value):
        self.find(locator_type, value).click()

    def send_keys(self, locator_type, value, text):
        self.find(locator_type, value).send_keys(text)

    def get_text(self, locator_type, value):
        el = self.driver.find_element(locator_type, value)
        return el.text

    '''Common Elements'''
    def click_back_arrow(self):
        self.click(*self.BackArrow)