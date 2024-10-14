import time
from pages.open_positions_page import OpenPositionsPage
from tests.base_test import BaseTest


class TestOpenPositions(BaseTest):
    def test_open_positions(self):
        open_positions_page = OpenPositionsPage(self.driver)
        open_positions_page.click_button_find_jobs()
        open_positions_page.open_location_dropdown()
        time.sleep(2)
        open_positions_page.select_location_turkey()
        open_positions_page.open_department_dropdown()
        time.sleep(2)
        open_positions_page.select_department_quality_assurance()
        open_positions_page.check_jobs_list()
        open_positions_page.check_position_title()
        open_positions_page.check_position_department()
        open_positions_page.check_position_location()
