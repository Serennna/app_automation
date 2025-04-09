from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

# 设置 Desired Capabilities（现在用 XCUITestOptions）
options = XCUITestOptions()
options.set_capability("platformName", "iOS")
options.set_capability("appium:deviceName", "iPhone14")
options.set_capability("appium:platformVersion", "16.5")
options.set_capability("appium:udid", "00008110-000948AE110A201E")
options.set_capability("appium:app", "live.fanatics.FanaticsCollect-Development")
options.set_capability("appium:automationName", "XCUITest")
options.set_capability("appium:includeSafariInWebviews", True)

# 连接 Appium Server，使用 options 参数而不是 desired_capabilities
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # 示例操作：点击登录按钮
    button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "login_button")
    button.click()
    time.sleep(2)
finally:
    driver.quit()
