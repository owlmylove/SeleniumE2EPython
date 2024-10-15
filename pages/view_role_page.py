import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ViewRole(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.view_role_button = (By.XPATH, "//*[text()='View Role']")
        self.view_role_redirect_url = (By.XPATH, "//*[@id='jobs-list']/div/div/a")
        self.lever_logo = (By.XPATH, "//*[text()='Lever logo'")
        self.lever_url = "https://jobs.lever.co/useinsider/"
        self.position_item_element = (By.CLASS_NAME, "position-list-item-wrapper")

    def check_redirect_url(self):
        self.wait_for_element_to_be_visible(self.view_role_button)
        href = self.find_element(self.view_role_redirect_url)
        for e in href:
            self.log(e.get_attribute('href'))

    def click_button_view_role(self):
        self.wait_for_element_to_be_visible(self.view_role_button).click()
        self.log('view role button is clicked')

    def check_view_role_redirect_button_href(self):
        self.log('check_view_role_redirect')
        view_button_href = self.scroll_to_element(self.view_role_button).get_attribute
        logging.info(view_button_href)
        assert (self.view_role_redirect_url in view_button_href)
        self.log(f'Redirect url is: {view_button_href}')

    def check_url(self):
        lever_logo_check = self.open_page(self.lever_url)
        url = lever_logo_check.get_url
        logging.info(url)
        assert (self.lever_url in url)
        self.log('url is correct')

    def check_lever_logo(self):
        self.open_page(self.lever_url)
        logo = self.driver.find_element(self.lever_logo)
        assert logo.is_displayed
        self.log('logo is present on page')