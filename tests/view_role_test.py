from pages.view_role_page import ViewRole
from tests.base_test import BaseTest


class TestViewRole(BaseTest):

    def test_view_role(self):
        view_page_page = ViewRole(self.driver)
        view_page_page.click_button_view_role()
        view_page_page.open_page("https://jobs.lever.co/useinsider/")
        view_page_page.check_view_role_redirect()
        view_page_page.check_lever_logo()
