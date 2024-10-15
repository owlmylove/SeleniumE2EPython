import unittest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import logging


class BaseTest(unittest.TestCase):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    def setUp(self):
        self.driver.implicitly_wait(10)
        logging.info('Open base url "https://useinsider.com/"')
        self.driver.get("https://useinsider.com/")

    def tearDown(self):
        self.driver.save_screenshot("../screenshots/error.png")
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    unittest.TextTestRunner(verbosity=1).run(suite)
