from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ViewRole(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.view_role_button = (By.XPATH, "//*[text()='View Role']")
        self.lever_logo = (By.CSS_SELECTOR, "img[alt='Lever logo']")
        self.lever_url = "https://jobs.lever.co/useinsider/"

    def click_button_view_role(self):
        self.hover(*self.view_role_button)
        self.find_element(*self.view_role_button).click()
        self.log('View role button is clicked')

    def check_view_role_redirect(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        assert self.lever_url in self.driver.current_url, "The url doesnt match"
        self.log('Redirect url is correct')

    def check_lever_logo(self):
        self.driver.find_element(*self.lever_logo).is_displayed()
        self.log('Logo is present on page')