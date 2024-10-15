import time

import pytest

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

## Screenshot methods are commented as they're integrated yet

# import pyautogui
# # Capture the entire screen
# screenshot = pyautogui.screenshot()
# # Save the screenshot to a file
# screenshot.save("screenshot_pyautogui.png")

# allure.step("Capture failure screenshot")
# def capture_failure_screenshot(driver):
#     driver.get_screenshot_as_file("failure_screenshot.png")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call" and report.failed:
#         item.instance.driver.save_screenshot("screenshots/screenshot_on_failure.png")


class TestSuite:

    def test_suite(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.implicitly_wait(10)
        #       self.driver = webdriver.Firefox
        driver.get("https://useinsider.com/")
        # driver.save_screenshot("screenshots/screenshot_on_failure.png")
        # driver.get_screenshot_as_file("screenshots/screenshot_on_failure.png")

        home_p = HomePage(driver)
        home_p.check_page_loaded()

        nav_page = NavigationMenu(driver)
        time.sleep(2)
        nav_page.check_navbar()
        time.sleep(2)
        nav_page.select_company()
        time.sleep(2)
        nav_page.select_careers()
        time.sleep(2)

        career_page = CareersPage(driver)
        time.sleep(2)
        career_page.check_page_element_locations()
        time.sleep(2)
        career_page.check_page_elements_teams()
        time.sleep(2)
        career_page.check_page_elements_lives()
        time.sleep(2)

        positions_page = OpenPositionsPage(driver)
        positions_page.click_button_find_jobs()
        positions_page.open_location_dropdown()
        time.sleep(2)
        positions_page.select_location_turkey()
        positions_page.open_department_dropdown()
        time.sleep(2)
        positions_page.select_department_quality_assurance()
        positions_page.check_jobs_list()
        positions_page.check_position_title()
        positions_page.check_position_department()
        positions_page.check_position_location()

        view_role = ViewRole(driver)
        view_role.click_button_view_role()
        view_role.open_page(view_role.view_role_redirect_url)
        view_role.check_view_role_redirect()
        view_role.check_lever_logo()

        driver.close()
