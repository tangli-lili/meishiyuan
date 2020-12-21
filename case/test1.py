
from appium import webdriver
from time import sleep

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
a = driver.get_window_size(windowHandle='current')
x = a['width']
y = a['height']
#点击分类
driver.find_element_by_id("com.meishio.app:id/card_default_item_category_icon").click()
sleep(2)
#点击农家产品
driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView').click()
sleep(2)
#点击蔬菜
driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[2]/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView').click()
sleep(2)
#点击红薯商品
driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView').click()
sleep(2)
#点击详情
driver.tap([(0.5*x,0.06*y)],500)
sleep(2)
#点击评价
driver.tap([(0.7*x,0.07*y)],500)
sleep(2)
# # #点击返回
# driver.tap([(0.06*x,0.07*y)],500)
# sleep(2)
#点击【加入购物车】
driver.tap([(0.37*x,0.96*y)],500)
sleep(2)
#登录
driver.find_element_by_id('com.meishio.app:id/user_login_username_email_phone').send_keys('username')
driver.find_element_by_id('com.meishio.app:id/user_login_password').send_keys('123456')
driver.find_element_by_id('com.meishio.app:id/user_login_btn').click()
sleep(2)
#登录成功后会进入到加入购物车页面，点击【加入购物车】
driver.tap([(0.37*x,0.96*y)],500)
sleep(2)
#点击确定
driver.find_element_by_id('com.meishio.app:id/product_properties_done').click()
sleep(2)
#加入成功，退出
driver.quit()


