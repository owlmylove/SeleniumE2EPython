from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

from utils.locators import HomePageLocators, NavigationMenuLocators, CareersPageLocators, OpenPositionsPageLocators


class BasePage(object):
    def __int__(self, driver, base_url='https://useinsider.com/'):
        self.base_url = base_url
        self.driver = driver
        self.locator = HomePageLocators
        self.locator = NavigationMenuLocators
        self.locator = CareersPageLocators
        self.locator = OpenPositionsPageLocators
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("Element was not found %(locator[1])")
            self.driver.quit()



