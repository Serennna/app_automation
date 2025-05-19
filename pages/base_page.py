from appium.webdriver.webdriver import WebDriver
from data.app_params import *
from typing import NoReturn, Optional
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

    def find(self, locator_type, value, index: Optional[int] = None):
        if index is None:
            return self.driver.find_element(locator_type, value)
        else:
            elements = self.driver.find_elements(locator_type, value)
            if index < len(elements):
                return elements[index]
            else:
                return False

    def click(self, locator_type, value, index: Optional[int] = None):
        self.find(locator_type, value, index).click()

    def send_keys(self, locator_type, value, text: str, index: Optional[int] = None):
        self.find(locator_type, value, index).send_keys(text)

    def get_text(self, locator_type, value, index: Optional[int] = None):
        el = self.find(locator_type, value, index)
        return el.text

    '''Common Elements'''

    def click_back_arrow(self):
        self.click(*self.BackArrow)
