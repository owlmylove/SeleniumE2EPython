import time
from pages.navigation_menu import NavigationMenu
from tests.base_test import BaseTest


class TestNavigation(BaseTest):
    def test_navigation_menu(self):
        navigation_menu = NavigationMenu(self.driver)
        navigation_menu.check_navbar()
        time.sleep(2)
        navigation_menu.select_company()
        time.sleep(2)
        navigation_menu.select_careers()
        time.sleep(2)
