from selenium.webdriver.common.by import By


class CareersPage:
    def __init__(self, driver):
        self.driver = driver
        self.element_Locations = (By.CSS_SELECTOR, "#career-our-location")
        self.element_Teams = (By.CSS_SELECTOR, "#career-find-our-calling")
        self.element_Lives = (By.XPATH, "//*[text()='Life at Insider']")

    def open_page(self, url):
        self.driver.get(url)

    def check_page_element_locations(self):
        self.driver.find_element(*self.element_Locations)
        assert self.element_Locations is not False
        print("Element Locations is present on Careers page")

    def check_page_elements_teams(self):
        self.driver.find_element(*self.element_Teams)
        assert self.element_Locations is not False
        print("Element Teams is present on Careers page")

    def check_page_elements_lives(self):
        self.driver.find_element(*self.element_Lives)
        assert self.element_Locations is not False
        print("Element Lives is present on Careers page")



