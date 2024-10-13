from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.check_page_logo = (By.CSS_SELECTOR, "#navigation [src*='logo-old.png']")

    def open_page(self, url):
        self.driver.get(url)

    def check_page_loaded(self):
        return True if self.driver.find_element(*self.check_page_logo) else False
