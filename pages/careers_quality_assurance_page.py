from selenium.webdriver.common.by import By


class QualityAssurancePage:
    def __init__(self, driver):
        self.driver = driver
        self.careers_quality_assurance_url = "https://useinsider.com/careers/quality-assurance/"
        self.see_allQaJobs_button = (By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a")  # See all QA jobs
        self.filter_location = (By.ID, "[id='select2-filter-by-location-container']")  # //*[@id="select2-filter-by-location-container"]
        self.filter_department = (By.ID, "[id='select2-filter-by-department-container']")  # //*[@id="select2-filter-by-department-container"]
        self.location_Turkey = (By.ID, "[id='select2-filter-by-location-result-y2n4-Istanbul, Turkey']")  # //*[@id="select2-filter-by-location-result-y2n4-Istanbul, Turkey"]
        self.department_qualityAssurance = (By.ID, "[id='select2-filter-by-department-result-2cey-Quality Assurance'']")
        self.positions_list = (By.ID, "[id='jobs-list'']")
        self.position_title = (By.CLASS_NAME, ".position-title")  # By.XPATH, "//*[text()='Quality Assurance']"
        self.position_department = (By.CLASS_NAME, ".position-department")  # Quality Assurance
        self.position_location = (By.CLASS_NAME, ".position-location")  # Istanbul, Turkey

    # open qa careers
    def open_page(self, url):
        self.driver.get(url)

    def click_button_all_qa_jobs(self):
        if self.driver.find_element(*self.see_allQaJobs_button).is_displayed():
            self.driver.see_allQaJobs_button.click()

    def check_department_is_qa(self):
        assert self.driver.filter_department in self.driver.filter_department("Quality Assurance").text

    def open_location_dropdown(self):
        self.driver.find_element(*self.filter_location).click()

    def select_location_turkey(self):
        self.driver.find_element(*self.location_Turkey).click()

    def check_jobs_list(self):
        assert self.driver.find_element(*self.positions_list).is_displayed() is not False
        print("Jobs list is on the page")

    def check_position_title(self):
        assert (self.driver.find_element(*self.position_title)
                in self.driver.position_title("Quality Assurance").text)

    def check_position_department(self):
        assert (self.driver.find_element(*self.position_department)
                in self.driver.position_department("Quality Assurance").text)

    def check_position_location(self):
        assert (self.driver.find_element(*self.position_location)
                in self.driver.position_location("Istanbul, Turkey").text)
