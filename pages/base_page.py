import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from data.app_params import *
from typing import NoReturn, Optional
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from typing import Optional
from utils.logger import setup_logger


class BasePage:
    BackArrow = (AppiumBy.ACCESSIBILITY_ID, 'Back')


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(driver,15)
        self.logger = setup_logger(self.__class__.__name__)


    '''App Actions'''

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
            self.logger.debug(f"Looking for element: {(locator_type, value)}")
            return self.wait.until(EC.presence_of_element_located((locator_type, value)))
        else:
            elements = self.wait.until(EC.presence_of_all_elements_located((locator_type, value)))
            if index < len(elements):
                return elements[index]
            else:
                self.logger.debug(f"Failed to find element: {(locator_type, value)}")
                return False

    def click(self, locator_type, value, index: Optional[int] = None):
        self.logger.debug(f"Clicking on element: {(locator_type, value)}")
        self.find(locator_type, value, index).click()

    def send_keys(self, locator_type, value, text: str, index: Optional[int] = None):
        self.logger.debug(f"Sending keys for element: {(locator_type, value)}")
        self.find(locator_type, value, index).send_keys(text)

    def get_text(self, locator_type, value, index: Optional[int] = None):
        el = self.find(locator_type, value, index)
        return el.text

    def is_displayed(self, locator_type, value, index: Optional[int] = None) -> bool:
        try:
            return self.find(locator_type, value, index).is_displayed()
        except:
            return False

    def get_attribute(self, locator_type, value, attribute: str, index: Optional[int] = None):
        return self.find(locator_type, value, index).get_attribute(attribute)
    '''Time wait'''

    def wait_until_visible(self, locator_type, value, timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(EC.visibility_of_element_located((locator_type, value)))

    def wait_until_clickable(self, locator_type, value, timeout: Optional[int] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(EC.element_to_be_clickable((locator_type, value)))

    '''Common actions'''
    def click_back_arrow(self):
        self.click(*self.BackArrow)

    def swipe_up(self, duration=500):
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_down(self, duration=500):
        size = self.driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] * 0.2
        end_y = size['height'] * 0.8
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def tap_by_coordinates(self, x, y):
        self.driver.tap([(x, y)])

    ''' tools '''
    def is_toast_present(self, message, timeout=5) -> bool:
        try:
            toast = (AppiumBy.XPATH, f"//*[contains(@label, '{message}')]")
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(toast))
            return True
        except:
            return False
