import time
from pages.view_role_page import ViewRolePage
from tests.base_test import BaseTest


class TestViewRole(BaseTest):

    def test_view_role(self):
        view_page_page = ViewRolePage(self.driver)
        view_page_page.click_button_view_role()
        time.sleep(1)
        view_page_page.open_page("https://jobs.lever.co/useinsider/")
        time.sleep(1)
        view_page_page.check_view_role_redirect()
        time.sleep(1)
        view_page_page.check_lever_logo()
