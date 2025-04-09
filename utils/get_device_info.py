import subprocess
import plistlib
import sys
from appium import webdriver
from data.app_params import app_environment, device_type,simulator_device_udid
from utils.driver_manager import config
from utils.common_tools import get_file_direction


def get_driver_on_real_device(no_rest):
    caps = webdriver.webdriver.AppiumOptions()
    device_info = get_device_info(get_app_name(app_environment), no_rest)
    for i in device_info.keys():
        caps.set_capability(i, device_info[i])
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=caps
    )
    driver.set_page_load_timeout(10)
    return driver


def get_device_on_simulator(no_rest=False):
    caps = webdriver.webdriver.AppiumOptions()
    caps.set_capability("platformName", "iOS")
    caps.set_capability("appium:automationName", "XCUITest")
    caps.set_capability('app', config['app'])
    caps.set_capability("appium:noReset", no_rest)
    # caps.set_capability("appium:resetStrategy", "appium")
    caps.set_capability("appium:udid",
                        simulator_device_udid if len(sys.argv) < 3 else sys.argv[1])  # change device udid
    caps.set_capability("appium:includeSafariInWebviews", True)
    caps.set_capability("appium:newCommandTimeout", 3600)
    caps.set_capability("appium:connectHardwareKeyboard", True)
    caps.set_capability("appium:enablePerformanceLogging", True)
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        options=caps
    )
    return driver


def get_driver(no_rest=False):
    if device_type == 'Real':
        return get_driver_on_real_device(no_rest)
    else:
        return get_device_on_simulator(no_rest)


# make sure installed unique app version
def get_app_name(app_type):
    file_direction = get_file_direction('ideviceinstaller')
    command = [file_direction, '-l', '-o', 'list_user']
    output = subprocess.check_output(command, universal_newlines=True)
    app_list = []
    lines = output.strip().split('\n')
    for line in lines:
        if 'live.fanatics' in line:
            app_list.append(line.split(',')[0])
    for app in app_list:
        if app_type in app:
            get_app = app
            return get_app


def get_simulator_devices():
    command = ['xcrun', 'simctl', 'list']
    output = subprocess.check_output(command, universal_newlines=True)
    devices_list = []
    lines = output.strip().split('\n')
    for line in lines:
        if 'iPhone' in line:
            devices_list.append(line)
    return devices_list


def get_plist_data():
    file_direction = get_file_direction('ideviceinfo')
    command = [file_direction, '-x']
    output = subprocess.check_output(command)
    plist_data = plistlib.loads(output)
    return plist_data


def get_device_info(app, no_rest):
    data = get_plist_data()
    device_info = {'appium:platformVersion': data.get('ProductVersion'),
                   'appium:deviceName': data.get('ProductType'),
                   'appium:udid': data.get('UniqueDeviceID'),
                   'platformName': 'iOS',
                   'appium:automationName': 'XCUITest',
                   'appium:noReset': no_rest,
                   'appium:includeSafariInWebviews': True,
                   'appium:connectHardwareKeyboard': True,
                   'appium:newCommandTimeout': 3600,
                   'appium:enablePerformanceLogging': True,
                   'app': app}

    return device_info


def start_wda():
    device_id = get_plist_data().get('UniqueDeviceID')
    print(device_id)
    cmd = f'xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination id={device_id} test'
    subprocess.Popen(cmd, shell=True)


def run_appium():
    file_direction = get_file_direction('ideviceinfo')
    command = [file_direction, '-x']
    output = subprocess.check_output(command)


get_device_info()