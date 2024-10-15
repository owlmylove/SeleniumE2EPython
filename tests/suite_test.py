from pages.home_page import HomePage
from pages.navigation_menu import NavigationMenu
from pages.careers_page import CareersPage
from pages.open_positions_page import OpenPositionsPage
from pages.view_role_page import ViewRole
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class TestSuite:

    def test_suite(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.implicitly_wait(10)
        driver.get("https://useinsider.com/")

        home_p = HomePage(driver)
        home_p.check_page_loaded()

        nav_page = NavigationMenu(driver)
        nav_page.check_navbar()
        nav_page.select_company()
        nav_page.select_careers()

        career_page = CareersPage(driver)
        career_page.check_page_element_locations()
        career_page.check_page_elements_teams()
        career_page.check_page_elements_lives()
        career_page.click_button_find_jobs()

        positions_page = OpenPositionsPage(driver)
        positions_page.open_location_dropdown()
        positions_page.select_location_turkey()
        positions_page.open_department_dropdown()
        positions_page.select_department_quality_assurance()
        positions_page.check_jobs_list()
#        positions_page.check_position_title()
        positions_page.check_position_department()
        positions_page.check_position_location()

        view_role = ViewRole(driver)
        view_role.check_view_role_redirect_button_href()
        view_role.click_button_view_role()
        view_role.check_redirect_url()
        view_role.check_lever_logo()

        driver.close()
