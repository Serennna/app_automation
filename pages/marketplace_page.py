from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from appium.webdriver.common.appiumby import AppiumBy

class MarketplacePage(BasePage):
    PROFILE_ICON = (AppiumBy.CLASS_NAME, "XCUIElementTypeImage")
    MARKETPLACE_TAB = (AppiumBy.XPATH,'''//XCUIElementTypeButton[@name="Marketplace"]''')
    BUY_NOW_PILL = (AppiumBy.ACCESSIBILITY_ID,'Buy Now')
    AUCTION_PILL = (AppiumBy.ACCESSIBILITY_ID,'Auction')
    PREMIER_AUCTION_PILL = (AppiumBy.ACCESSIBILITY_ID,'Premier Auction')
    SEARCH_BAR =  (AppiumBy.ACCESSIBILITY_ID,'search')

    def __init__(self, driver):
        super().__init__(driver)

    '''actions'''
    def navigate_to_marketplace(self):
        """导航到Marketplace标签页"""
        if not self.is_marketplace_tab_active():
            self.click(*self.MARKETPLACE_TAB)
            self.wait.until(lambda d: self.is_marketplace_tab_active())
        return self

    def click_marketplace_tab(self):
        self.find(*self.MARKETPLACE_TAB).click()

    def click_buy_now_pill(self):
        self.click(*self.BUY_NOW_PILL)

    def click_buy_aucion_pill(self):
        self.click(*self.AUCTION_PILL)

    def click_buy_premiee_aucion_pill(self):
        self.click(*self.PREMIER_AUCTION_PILL)

    ''' status Check'''
    def is_logged_in(self):
        ''' check log-in status'''
        try:
            self.find(*self.PROFILE_ICON,index=1)
            return True
        except:
            return False

    def ensure_marketplace_with_login_check(self, email, password):
        ''' make sure user logged in already '''
        if not self.is_logged_in():
            # back to home paeg
            home_page = HomePage(self.driver)
            home_page.go_to_login_page()

            # then login using test account
            login_page = LoginPage(self.driver)
            login_page.login(email, password)
        else:
            self.click_marketplace_tab()
        return self

    def is_marketplace_tab_active(self):
        """检查当前是否在Marketplace标签页"""
        return self.is_displayed(*self.SEARCH_BAR)

