from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import Interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput

from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class CheckoutPage(BasePage):

    ORDER_SUMMARY = (AppiumBy.ACCESSIBILITY_ID,'Order Summary')
    SHIP_TO_VAULT = (AppiumBy.ACCESSIBILITY_ID,'Ship to Collect Vault')
    SLIDE_TO_PAY = (AppiumBy.ACCESSIBILITY_ID,'Slide to pay')
    ORDER_PLACED= (AppiumBy.ACCESSIBILITY_ID,'order_gradient')
    COMPLETE_LABEL = (AppiumBy.ACCESSIBILITY_ID,'COMPLETE')
    DONE_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Done')



    def __init__(self, driver):
        super().__init__(driver)

    def slide_to_pay(self):
        # get button position
        slider = self.find(*self.SLIDE_TO_PAY)
        start_x = slider.location['x'] + slider.size['width'] / 2
        start_y = slider.location['y'] + slider.size['height'] / 2
        end_x = start_x + 200

        # Finger Action
        finger = PointerInput(Interaction, "finger")
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=finger)

        # 3.W3C PointerInput
        finger = PointerInput("touch", "finger")
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=finger)

        # 4. Slide
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, start_y)
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()