import unittest
from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        #       self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("https://useinsider.com/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    unittest.TextTestRunner(verbosity=1).run(suite)
