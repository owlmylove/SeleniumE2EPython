from selenium.webdriver.common.by import By


class NavigationMenu:
    def __init__(self, driver):
        self.driver = driver
        self.navigation_bar = (By.CSS_SELECTOR, "[id='navbarNavDropdown']")
        self.dropdown_menu = (By.CLASS_NAME, "dropdown-menu new-menu-dropdown-layout-6 show")
        self.element_Company = (By.XPATH, "//*[@id='navbarNavDropdown']/ul[1]/li[6]")
        self.element_Careers = (By.XPATH, "//*[text()='Careers']")
        self.careers_url = "https://useinsider.com/careers/"

    def check_navbar(self):
        self.driver.find_element(*self.navigation_bar)
        assert self.navigation_bar is not False, "Navigation Bar is not on a screen"
        print("Navigation Bar is present on a screen")

    def select_company(self):
        self.driver.find_element(*self.element_Company).click()
        assert self.dropdown_menu is not False, "Dropdown menu has not open"
        print("Dropdown menu has shown")

    def select_careers(self):
        self.driver.find_element(*self.element_Careers).click()
        assert self.driver.current_url.find(self.careers_url) is not False, "Careers page has not open"
        print("Careers page is open")









