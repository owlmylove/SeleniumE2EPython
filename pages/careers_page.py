from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.element_Locations = (By.CSS_SELECTOR, "#career-our-location")
        self.element_Teams = (By.CSS_SELECTOR, "#career-find-our-calling")
        self.element_Lives = (By.XPATH, "//*[text()='Life at Insider']")
        self.find_jobs_button_Careers = (By.XPATH, "//*[@id='page-head']//a[text()='Find your dream job']")

    def check_page_element_locations(self):
        self.wait_for_element_to_be_visible(*self.element_Locations)
        self.log('check_page_element_locations')

    def check_page_elements_teams(self):
        self.wait_for_element_to_be_visible(*self.element_Teams)
        self.log('check_page_elements_teams')

    def check_page_elements_lives(self):
        self.driver.wait_for_element_to_be_visible(*self.element_Lives)
        self.log('check_page_elements_lives')

    def click_button_find_jobs(self):
        self.driver.wait_for_element_to_be_visible(*self.find_jobs_button_Careers).click()
        self.log('lick_button_find_jobs')

