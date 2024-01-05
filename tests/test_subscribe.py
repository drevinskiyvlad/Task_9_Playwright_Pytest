import pytest
from playwright.sync_api import Page

from pages.main_page import MainPage
from utils.faker import Faker
from utils.tools import take_screenshot


class TestSubscribe:
    @pytest.fixture()
    def test_setup(self, new_page: Page):
        self.page = new_page

        self.main_page = MainPage(self.page)
        self.faker = Faker()

    @pytest.mark.subscribe
    def test_subscribe(self, test_setup):
        valid_email = self.faker.generate_valid_email()

        self.main_page.verify_page()
        self.main_page.subscribe(valid_email)
        self.main_page.verify_subscribe_success_message()

        take_screenshot(self.page, "Subscribe")
