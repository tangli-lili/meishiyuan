from appium.webdriver.common.mobileby import By
from page.base_page import BasePage
from time import sleep
class ShoppingCarPage(BasePage):
    classify_locator=(By.ID,'com.meishio.app:id/card_default_item_category_icon')
    farmproduce_locator=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.widget.TextView')
    vegetables_locator=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView[2]/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView')
    sweetpotato_locator=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView')
    username_locator=(By.ID,'com.meishio.app:id/user_login_username_email_phone')
    password_locator=(By.ID,'com.meishio.app:id/user_login_password')
    denglu_locator=(By.ID,'com.meishio.app:id/user_login_btn')
    ok_locator=(By.ID,'com.meishio.app:id/product_properties_done')



    def click_classify(self):
        self.find_element(self.classify_locator).click()
    def click_farmproduce(self):
        self.find_element(self.farmproduce_locator).click()
    def click_vegetables(self):
        self.find_element(self.vegetables_locator).click()
    def click_sweetpotato(self):
        self.find_element(self.sweetpotato_locator).click()
    def sendkeys_username(self,username):
        self.find_element(self.username_locator).send_keys(username)
    def sendkeys_password(self,password):
        self.find_element(self.password_locator).send_keys(password)
    def click_denglu(self):
        self.find_element(self.denglu_locator).click()
    def click_ok(self):
        self.find_element(self.ok_locator).click()

    def addcar(self,username,password):
        self.click_classify()
        self.click_farmproduce()
        self.click_vegetables()
        self.click_sweetpotato()
        sleep(1)
        self.tap_eleement(533, 131,500)
        sleep(1)
        self.tap_eleement(774, 131,500)
        sleep(1)
        self.tap_eleement(71,146,500)
        sleep(1)
        self.tap_eleement(448, 1831,500)
        sleep(1)
        self.sendkeys_username(username)
        self.sendkeys_password(password)
        self.click_denglu()
        sleep(1)
        self.tap_eleement(436,1847,500)
        sleep(1)
        self.click_ok()




