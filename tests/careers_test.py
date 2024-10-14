import time
from pages.careers_page import CareersPage
from tests.base_test import BaseTest


class TestCareers(BaseTest):
    def test_careers(self):
        careers_page = CareersPage(self.driver)
        careers_page.element_Locations()
        time.sleep(1)
        careers_page.element_Teams()
        time.sleep(1)
        careers_page.element_Lives()
        time.sleep(1)
