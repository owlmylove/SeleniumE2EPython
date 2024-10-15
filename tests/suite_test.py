import time

from pages.home_page import HomePage
from pages.navigation_menu import NavigationMenu
from pages.careers_page import CareersPage
from pages.open_positions_page import OpenPositionsPage
from pages.view_role_page import ViewRole
from tests.base_test import BaseTest


class TestSuite(BaseTest):

    def test_suite(self):

        home_p = HomePage(self.driver)
        home_p.check_page_loaded()

        nav_page = NavigationMenu(self.driver)
        nav_page.check_navbar()
        nav_page.select_company()
        nav_page.select_careers()

        career_page = CareersPage(self.driver)
        career_page.check_page_element_locations()
        career_page.check_page_elements_teams()
        career_page.check_page_elements_lives()

        career_page.click_button_find_jobs()  # close cookie pop-up here to continue test

        positions_page = OpenPositionsPage(self.driver)
        positions_page.open_location_dropdown()
        positions_page.select_location_turkey()
        positions_page.open_department_dropdown()
        positions_page.select_department_quality_assurance()
        positions_page.check_jobs_list()
        time.sleep(5)
        positions_page.check_position_title()
        time.sleep(5)
        positions_page.check_position_department()
        time.sleep(5)
        positions_page.check_position_location()
        time.sleep(5)

        view_role = ViewRole(self.driver)
#        view_role.check_redirect_url()
        view_role.click_button_view_role()  # scroll down to the QA job item and hover to make button "View Role" visible
        time.sleep(5)
        # view_role.check_view_role_redirect_button_href()
        # view_role.check_redirect_url()
        # view_role.check_lever_logo()

