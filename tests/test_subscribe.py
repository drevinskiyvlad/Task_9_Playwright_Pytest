import pytest
from playwright.sync_api import Page

from helper.faker import Faker
from pages.contact_us_page import ContactUsPage
from pages.main_page import MainPage


class TestSubscribe:
    @pytest.fixture()
    def test_setup(self, page: Page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})

        self.main_page = MainPage(self.page)
        self.faker = Faker()

    def test_subscribe(self, test_setup):
        valid_email = self.faker.generate_valid_email()

        self.main_page.visit()
        self.main_page.verify_page()
        self.main_page.subscribe(valid_email)
        self.main_page.verify_subscribe_success_message()
