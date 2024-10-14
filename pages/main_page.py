from pages.base_page import BasePage
from pages.careers_page import CareersPage
from pages.careers_quality_assurance_page import QualityAssurancePage
from pages.home_page import HomePage
from pages.view_role_page import ViewRolePage
from pages.open_positions_page import OpenPositionsPage
from pages.navigation_menu import NavigationMenu


class TestSuite(BasePage):
    def __init__(self, driver):
        self.driver = driver



