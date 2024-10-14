from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.element_Locations = (By.CSS_SELECTOR, "#career-our-location")
        self.element_Teams = (By.CSS_SELECTOR, "#career-find-our-calling")
        self.element_Lives = (By.XPATH, "//*[text()='Life at Insider']")

    def check_page_element_locations(self):
        self.driver.find_element(*self.element_Locations)
        assert self.element_Locations is not False

    def check_page_elements_teams(self):
        self.driver.find_element(*self.element_Teams)
        assert self.element_Locations is not False

    def check_page_elements_lives(self):
        self.driver.find_element(*self.element_Lives)
        assert self.element_Locations is not False
