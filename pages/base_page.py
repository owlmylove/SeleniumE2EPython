from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage(object):
    def __int__(self, driver, base_url='https://useinsider.com/'):
        self.base_url = base_url
        self.driver = driver
        self.wait_element = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
#        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def get_page_title(self):
        page_title = self.driver.title
        return page_title

    def scroll_to_element(self, locator):
        self.driver.execute_script(
            "arguments[0].scrollIntoView()", self.driver.find_element(By.XPATH, locator))

    def wait_for_element_to_be_visible(self, locator):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("Element was not found %(locator[1])")
            self.driver.quit()
