from selenium.webdriver.common.by import By


class QualityAssurancePage:
    def __init__(self, driver):
        self.driver = driver
        self.careers_quality_assurance_url = "https://useinsider.com/careers/quality-assurance/"
        self.see_allQaJobs_button = (By.CLASS_NAME, ".btn-outline-secondary")  # See all QA jobs
        self.filter_location = (By.ID, "[id='select2-filter-by-location-container']")  # //*[@id="select2-filter-by-location-container"]
        self.filter_department = (By.ID, "[id='select2-filter-by-department-container']")  # //*[@id="select2-filter-by-department-container"]
        self.location_Turkey = (By.ID, "[id='select2-filter-by-location-result-y2n4-Istanbul, Turkey']")  # //*[@id="select2-filter-by-location-result-y2n4-Istanbul, Turkey"]
        self.department_qualityAssurance = (By.ID, "[id='select2-filter-by-department-result-2cey-Quality Assurance'']")
        self.positions_list = (By.ID, "[id='jobs-list'']")
        self.position_title = (By.CLASS_NAME, ".position-title")  # By.XPATH, "//*[text()='Quality Assurance']"
        self.position_title = (By.CLASS_NAME, ".position-department")  # Quality Assurance
        self.position_title = (By.CLASS_NAME, ".position-location")  # Istanbul, Turkey

    # open qa careers
    def open_page(self, url):
        self.driver.get(url)

    def check_page_element_locations(self):
        self.driver.find_element(*self.element_Locations)
        assert self.element_Locations is not False
        print("Element Locations is present on Careers page")

    def open_openPositions_page(self):
        self.driver.find_element(*self.element_Careers).click()
        assert self.driver.current_url.find(self.careers_url) is not False, "Careers page has not open"
        print("Careers page is open")

