import time
from pages.open_positions_page import OpenPositionsPage
from tests.base_test import BaseTest


class TestOpenPositions(BaseTest):
    def test_open_positions(self):
        open_positions_page = OpenPositionsPage(self.driver)
        open_positions_page.click_button_find_jobs()
        time.sleep(1)
        open_positions_page.open_location_dropdown()
        time.sleep(2)
        open_positions_page.select_location_turkey()
        time.sleep(1)
        open_positions_page.open_department_dropdown()
        time.sleep(2)
        open_positions_page.select_department_quality_assurance()
        time.sleep(1)
        open_positions_page.check_jobs_list()
        time.sleep(1)
        open_positions_page.check_position_title()
        time.sleep(1)
        open_positions_page.check_position_department()
        time.sleep(1)
        open_positions_page.check_position_location()
        time.sleep(1)
