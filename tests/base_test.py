import unittest
from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
#        self.driver = webdriver.Firefox
        self.driver.get("https://useinsider.com/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BasePage)
    unittest.TextTestRunner(verbosity=1).run(suite)
