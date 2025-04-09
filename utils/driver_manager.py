from appium import webdriver
from appium.options.ios import XCUITestOptions
from utils.config_loader import load_config

config = load_config()
def create_driver():
    options = XCUITestOptions()
    for key, value in config.items():
        if key != "appiumServer":
            options.set_capability(f"appium:{key}", value)
    return webdriver.Remote(config['appiumServer'], options=options)