from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import logging
from datetime import datetime


class BasePage(object):
    def __int__(self, driver, base_url='https://useinsider.com/'):
        self.base_url = base_url
        self.driver = driver
        self.wait_element = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def wait_for_element_to_be_visible(self, locator):
        wait = WebDriverWait(self.driver, 30)
        self.log(f'wait_for_element_to_be_visible {locator}')
        return wait.until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        self.driver.execute_script(
            "arguments[0].scrollIntoView()", self.driver.find_element(*locator))

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_text(self, element):
        self.log(f'get_text: {element}')
        return self.driver.find_element(*element).get_property('innerText')

    def log(self, text):
        self.driver.save_screenshot(f'../screenshots/step_{datetime.now()}.png')
        logging.info(text)

    def accept_cookies(self, element):
        try:
            self.log('Accept cookies')
            self.wait_for_element_to_be_visible(element).click()
            self.log('Cookies accepted')
        except Exception as e:
            self.log(f'An error occured: {e}')
