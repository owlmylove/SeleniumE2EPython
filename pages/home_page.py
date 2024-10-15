from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page_logo = (By.CSS_SELECTOR, "#navigation [src*='logo-old.png']")

    def check_page_loaded(self):
        self.log('Home page opened')
        return True if self.find_element(*self.check_page_logo) else False

