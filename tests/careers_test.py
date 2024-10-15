from pages.careers_page import CareersPage
from tests.base_test import BaseTest
# from pages.base_page import BasePage


class TestCareers(BaseTest):
    def test_careers(self):
        careers_page = CareersPage(self.driver)
        careers_page.check_page_element_locations()
        careers_page.check_page_elements_teams()
        careers_page.check_page_elements_lives()
