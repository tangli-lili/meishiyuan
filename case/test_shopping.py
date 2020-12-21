import unittest
from case.base_case import BaseCase
from page.shopping_car_page import ShoppingCarPage
from model.read_datas import readexcel

class Mytest(BaseCase):
    def test_a(self):
        username,password= readexcel('')[0]
        print("-----------")
        ShoppingCarPage(self.driver).addcar(username,password)
if __name__ == '__main__':
    unittest.main()
