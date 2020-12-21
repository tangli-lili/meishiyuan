
from appium import webdriver
def start_app():
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platVersion': '7.1.2',
        'noReset': True,
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'newCommandTimeout': 600,
        'appPackage': 'com.meishio.app',
        'appActivity': 'module.home.activity.SplashActivity'
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.implicitly_wait(30)
    return driver