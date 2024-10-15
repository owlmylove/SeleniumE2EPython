from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ViewRole(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.view_role_button = (By.XPATH, "//*[text()='View Role']")
        self.view_role_redirect_url = (By.CSS_SELECTOR, "[content^='https://jobs.lever.co/useinsider/']")
        self.lever_logo = (By.XPATH, "//*[text()='Lever logo'")
        self.lever_url = "https://jobs.lever.co/useinsider/"

# hover

    def click_button_view_role(self):
        self.log('click_button_view_role')
        view_button = self.wait_for_element_to_be_visible(*self.view_role_button)
        view_button.click()
        self.log('button view role is clicked')
 #       print(self.driver.find_element(*self.view_role_button).__getattribute__('href').click())

    def check_view_role_redirect(self):
        self.driver.find_element(*self.view_role_redirect_url)
        assert self.driver.current_url.find(self.view_role_redirect_url) is not False

    def check_lever_logo(self):
        self.driver.find_element(*self.lever_logo)
        return True if self.driver.find_element(*self.lever_logo) else False

