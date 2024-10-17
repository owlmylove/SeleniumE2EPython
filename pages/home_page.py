from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page_logo = (By.CSS_SELECTOR, "#navigation [src*='logo-old.png']")
        self.locator_cookies = (By.CSS_SELECTOR, ".cli-wrapper #wt-cli-accept-all-btn")

    def check_page_loaded(self):
        self.log('Home page opened')
        assert self.find_element(*self.check_page_logo) is not False
        self.accept_cookies(self.locator_cookies)

