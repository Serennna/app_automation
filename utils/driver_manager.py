from appium import webdriver
from appium.options.ios import XCUITestOptions
from utils.config_loader import load_config
from utils.common_tools import get_connected_uuid
from utils.logger import setup_logger
import logging
from typing import Optional

logger = setup_logger(__name__)

from appium import webdriver
from appium.options.ios import XCUITestOptions
from utils.config_loader import load_config
from utils.common_tools import get_connected_uuid

class DriverManager:
    @staticmethod
    def get_driver():
        config = load_config()

        # 自动填充 UDID（如果没有指定或是占位符）
        if not config.get("udid") or config["udid"] == "auto":
            config["udid"] = get_connected_uuid()

        options = XCUITestOptions()
        for key, value in config.items():
            if key != "appiumServer":
                options.set_capability(f"appium:{key}", value)

        return webdriver.Remote(config["appiumServer"], options=options)