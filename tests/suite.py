import time
from pages.home_page import HomePage
from pages.navigation_menu import NavigationMenu
from pages.careers_page import CareersPage
from pages.base_page import BasePage
from tests.home_page_test import TestHomePage
from tests.navigation_test import TestNavigation
from tests.careers_test import TestCareers
from tests.base_test import BaseTest


class Suite(BaseTest):

    def suite(self):
        home_page = HomePage(self.driver)
        nav_page = NavigationMenu(self)
        careers_page = CareersPage(self)
        base_page = BasePage()
        home_page.check_page_loaded()
        time.sleep(5)
        nav_page.check_navbar()
        nav_page.select_company()
        nav_page.select_careers()
        base_page.get_url()
        careers_page.check_page_element_locations()
        careers_page.check_page_elements_teams()
        careers_page.check_page_elements_lives()



