import pytest
from playwright.sync_api import Page

from pages.contact_us_page import ContactUsPage
from pages.main_page import MainPage
from utils.faker import Faker
from utils.tools import take_screenshot


class TestContactUs:
    @pytest.fixture()
    def test_setup(self, new_page: Page):
        self.page = new_page

        self.main_page = MainPage(self.page)
        self.contact_us_page = ContactUsPage(self.page)
        self.faker = Faker()

    @pytest.mark.contact_us
    def test_contact_us(self, test_setup):
        valid_name = self.faker.generate_random_string(6)
        valid_email = self.faker.generate_valid_email()
        valid_subject = self.faker.generate_random_string(6)
        valid_message = self.faker.generate_random_string(6)

        self.main_page.verify_page()
        self.main_page.click_contact_us_link()

        self.contact_us_page.handle_alert()
        self.contact_us_page.send_message(valid_name, valid_email, valid_subject, valid_message)
        self.contact_us_page.verify_success_message()

        take_screenshot(self.page, "Contact Us")
