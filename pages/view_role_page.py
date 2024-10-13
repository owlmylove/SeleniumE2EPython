from selenium.webdriver.common.by import By


class ViewRolePage:
    def __init__(self, driver):
        self.driver = driver
        self.view_role_button = (By.XPATH, "//*[text()='View Role']")
        self.view_role_redirect_url = (By.CSS_SELECTOR, "[content^='https://jobs.lever.co/useinsider/']")
        self.lever_logo = (By.XPATH, "//*[text()='Lever logo'")

    def open_page(self, url):
        self.driver.get(url)

    def hover_button_view_role(self):
        self.driver.find_element(*self.element_Locations)
        assert self.element_Locations is not False
        print("Element Locations is present on Careers page")

    def click_button_view_rule(self):
        self.driver.find_element(*self.element_Careers).click()
        assert self.driver.current_url.find(self.careers_url) is not False, "Careers page has not open"
        print("Careers page is open")

    def check_view_rule_redirect(self):
        self.driver.find_element(*self.element_Careers).click()
        assert self.driver.current_url.find(self.careers_url) is not False, "Careers page has not open"
        print("Careers page is open")

