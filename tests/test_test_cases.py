import pytest
from playwright.sync_api import Page

from pages.cases_page import CasesPage
from pages.main_page import MainPage
from utils.tools import take_screenshot


class TestTestCases:
    @pytest.fixture()
    def test_setup(self, new_page: Page):
        self.page = new_page

        self.main_page = MainPage(self.page)
        self.test_cases_page = CasesPage(self.page)

    def test_verify_test_cases_page(self, test_setup):
        self.main_page.verify_page()
        self.main_page.click_test_cases_link()
        self.test_cases_page.verify_page()

        take_screenshot(self.page, "Verify Test Cases Page")
