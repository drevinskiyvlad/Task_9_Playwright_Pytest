import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage
from pages.test_cases_page import TestCasesPage


class TestTestCases:
    @pytest.fixture()
    def test_setup(self, page: Page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})

        self.main_page = MainPage(self.page)
        self.test_cases_page = TestCasesPage(self.page)

    def test_verify_test_cases_page(self, test_setup):
        self.main_page.visit()
        self.main_page.verify_page()
        self.main_page.click_test_cases_link()
        self.test_cases_page.verify_page()
