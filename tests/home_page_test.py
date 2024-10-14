from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestHomePage(BaseTest):
    def test_home_page(self):
        home_page = HomePage(self.driver)
        home_page.check_page_loaded()
