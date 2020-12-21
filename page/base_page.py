class BasePage():
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,locator):
        return self.driver.find_element(*locator)
    def tap_eleement(self,x,y,time):
        a = self.driver.get_window_size(windowHandle='current')
        print(a['width'])
        xx= int(a['width']*x/1080)
        yy= int(a['height']*y/1920)
        self.driver.tap([(xx,yy)],time)



