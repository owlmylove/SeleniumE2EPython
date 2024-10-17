import time
import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OpenPositionsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.filter_location = (By.XPATH, "//*[@id='select2-filter-by-location-container']")
        self.filter_department = (By.XPATH, "//*[@id='select2-filter-by-department-container']")
        self.location_Turkey = (By.XPATH, "//*[text()='Istanbul, Turkey']")
        self.department_qualityAssurance = (By.XPATH, "//*[text()='Quality Assurance']")  # "//*[contains(@id, 'Quality Assurance')]"
        self.positions_list = (By.XPATH, "//*[@id='jobs-list']")
        self.position_title = (By.CLASS_NAME, "position-title")  # Quality Assurance
        self.position_department = (By.CLASS_NAME, "position-department")  # Quality Assurance
        self.position_location = (By.CLASS_NAME, "position-location")  # Istanbul, Turkey
        self.open_positions_url = "https://useinsider.com/careers/open-positions/"

    def open_location_dropdown(self):
        time.sleep(1)
        self.log('open_location_dropdown')
        location = self.wait_for_element_to_be_visible(self.filter_location)
        if location.is_displayed():
            location.click()
            self.log('clicked on dropdown')

    def select_location_turkey(self):
        self.log('select_location_turkey')
        turkey = self.wait_for_element_to_be_visible(self.location_Turkey)
        if turkey.is_displayed():
            turkey.click()
            self.log('clicked on turkey')

    def open_department_dropdown(self):
        self.log('open_department_dropdown')
        department = self.wait_for_element_to_be_visible(self.filter_department)
        if department.is_displayed():
            department.click()
            self.log('clicked on department')

    def select_department_quality_assurance(self):
        self.log('select_department_quality_assurance')
        qa = self.wait_for_element_to_be_visible(self.department_qualityAssurance)
        if qa.is_displayed():
            qa.click()

    def check_jobs_list(self):
        time.sleep(3)
        self.log('check_jobs_list')
        assert self.wait_for_element_to_be_visible(self.positions_list).is_displayed is not False
        self.scroll_to_element(self.positions_list)

    def check_position_title(self):
        self.log('check_position_title')
        title_p = self.get_text(self.position_title)
        logging.info(title_p)
        assert ("Quality Assurance" in title_p)
        self.log(f'position_title is: {title_p}')

    def check_position_department(self):
        self.log('check_position_department')
        title_d = self.get_text(self.position_department)
        logging.info(title_d)
        assert ("Quality Assurance" in title_d)
        self.log(f'position_department is: {title_d}')

    def check_position_location(self):
        self.log('check_position_location')
        title_l = self.get_text(self.position_location)
        logging.info(title_l)
        assert ("Istanbul, Turkey" in title_l)
        self.log(f'position_location is: {title_l}')
