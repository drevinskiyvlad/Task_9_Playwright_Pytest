import pytest
from playwright.sync_api import Page

from helper.faker import Faker
from pages.contact_us_page import ContactUsPage
from pages.main_page import MainPage


class TestContactUs:
    @pytest.fixture()
    def test_setup(self, page: Page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})

        self.main_page = MainPage(self.page)
        self.contact_us_page = ContactUsPage(self.page)
        self.faker = Faker()

        self.main_page.visit()
        self.main_page.verify_page()
        self.main_page.click_contact_us_btn()

    def test_contact_us(self, test_setup):
        valid_name = self.faker.generate_random_string(6)
        valid_email = self.faker.generate_valid_email()
        valid_subject = self.faker.generate_random_string(6)
        valid_message = self.faker.generate_random_string(6)

        self.contact_us_page.handle_alert()
        self.contact_us_page.send_message(valid_name, valid_email, valid_subject, valid_message)
        self.contact_us_page.verify_success_message()