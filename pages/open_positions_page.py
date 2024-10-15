import time

from selenium.webdriver.common.by import By


class OpenPositionsPage:
    def __init__(self, driver):
        self.driver = driver
        self.find_jobs_button_Careers = (By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a")
        self.filter_location = (By.XPATH, "//*[@id='select2-filter-by-location-container']")
        self.filter_department = (By.XPATH, "//*[@id='select2-filter-by-department-container']")
        self.location_Turkey = (By.XPATH, "//*[@id='select2-filter-by-location-result-y2n4-Istanbul, Turkey']")
        self.department_qualityAssurance = (
            By.XPATH, "//*[@id='select2-filter-by-department-result-2cey-Quality Assurance']")
        self.positions_list = (By.XPATH, "//*[@id='jobs-list']")
        self.position_title = (By.CLASS_NAME, ".position-title")  # Quality Assurance
        self.position_department = (By.CLASS_NAME, ".position-department")  # Quality Assurance
        self.position_location = (By.CLASS_NAME, ".position-location")  # Istanbul, Turkey
        self.open_positions_url = "https://useinsider.com/careers/open-positions/"

    #      self.open_positions_quality_assurance_url = "https://useinsider.com/careers/open-positions/?department=qualityassurance"

    def click_button_find_jobs(self):
        if self.driver.find_element(*self.find_jobs_button_Careers).click():
            assert self.driver.current_url.find(self.open_positions_url) is not False

    def open_location_dropdown(self):
        location = self.driver.find_element(*self.filter_location)
        time.sleep(5)
        if location.is_displayed():
            location.click()

    def select_location_turkey(self):
        turkey = (self.driver.find_element(*self.location_Turkey)).wait_for_element_to_be_visible
        if turkey.is_displayed():
            turkey.click()

    def open_department_dropdown(self):
        department = self.driver.find_element(*self.filter_department)
        time.sleep(5)
        if department.is_displayed():
            department.click()

    def select_department_quality_assurance(self):
        qa = (self.driver.find_element(*self.department_qualityAssurance)).wait_for_element_to_be_visible
        if qa.is_displayed():
            qa.click()

    def check_jobs_list(self):
        assert self.driver.find_element(*self.positions_list).is_displayed() is not False

    def check_position_title(self):
        assert (self.driver.find_element(*self.position_title)
                in self.driver.position_title("Quality Assurance").text)

    def check_position_department(self):
        assert (self.driver.find_element(*self.position_department)
                in self.driver.position_department("Quality Assurance").text)

    def check_position_location(self):
        assert (self.driver.find_element(*self.position_location)
                in self.driver.position_location("Istanbul, Turkey").text)
