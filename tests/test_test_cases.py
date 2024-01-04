import pytest
from playwright.sync_api import Page

from pages.cases_page import TestCasesPage
from pages.main_page import MainPage


class TestTestCases:
    @pytest.fixture()
    def test_setup(self, new_page: Page):
        self.page = new_page

        self.main_page = MainPage(self.page)
        self.test_cases_page = TestCasesPage(self.page)

    def test_verify_test_cases_page(self, test_setup):
        self.main_page.verify_page()
        self.main_page.click_test_cases_link()
        self.test_cases_page.verify_page()
