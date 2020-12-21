from model.satrt_app import start_app
import unittest
class BaseCase(unittest.TestCase):
    def setUp(self):
        self.driver=start_app()
    # def tearDown(self):
    #     self.driver.quite()
