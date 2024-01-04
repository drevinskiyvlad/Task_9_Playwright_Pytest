import pytest

from playwright.sync_api import Page

from helper.faker import Faker
from pages.account_created_page import AccountCreatedPage
from pages.delete_account_page import DeleteAccountPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.signup_page import SignupPage


class TestLogin:
    @pytest.fixture()
    def test_setup(self, page: Page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})

        self.main_page = MainPage(self.page)
        self.login_page = LoginPage(self.page)
        self.signup_page = SignupPage(self.page)
        self.account_created_page = AccountCreatedPage(self.page)
        self.delete_account_page = DeleteAccountPage(self.page)
        self.faker = Faker()

        self.main_page.visit()
        self.main_page.verify_page()
        self.main_page.click_login_btn()

    def test_register(self, test_setup):
        valid_name = self.faker.generate_random_string(6)
        valid_email = self.faker.generate_valid_email()

        self.login_page.verify_register()
        self.login_page.signup(valid_name, valid_email)
        self.signup_page.verify_enter_information_msg()

        valid_gender = self.faker.generate_random_number_in_range(1, 2)
        valid_password = self.faker.generate_random_string(8)
        valid_day = str(self.faker.generate_random_number_in_range(1, 31))
        valid_month = str(self.faker.generate_random_number_in_range(1, 12))
        valid_year = str(self.faker.generate_random_number_in_range(1900, 2021))

        self.signup_page.enter_account_information(valid_gender,
                                                   valid_password,
                                                   valid_day,
                                                   valid_month,
                                                   valid_year)

        valid_firstname = self.faker.generate_random_string(6)
        valid_lastname = self.faker.generate_random_string(6)
        valid_company = self.faker.generate_random_string(6)
        valid_address1 = self.faker.generate_random_string(6)
        valid_address2 = self.faker.generate_random_string(6)
        valid_country = self.faker.generate_random_country()
        valid_state = self.faker.generate_random_string(6)
        valid_city = self.faker.generate_random_string(6)
        valid_zipcode = str(self.faker.generate_random_number_with_length(5))
        valid_mobile_number = str(self.faker.generate_random_number_with_length(10))

        self.signup_page.enter_address_information(valid_firstname,
                                                   valid_lastname,
                                                   valid_company,
                                                   valid_address1,
                                                   valid_address2,
                                                   valid_country,
                                                   valid_state,
                                                   valid_city,
                                                   valid_zipcode,
                                                   valid_mobile_number)

        self.signup_page.click_create_account_btn()

        self.account_created_page.verify_account_created_msg()
        self.account_created_page.click_continue_btn()
        self.main_page.verify_page()
        self.main_page.verify_logged_in_user()
        self.main_page.click_delete_account_btn()

        self.delete_account_page.verify_account_deleted_msg()
        self.delete_account_page.click_continue_btn()

    # def test_login(self, test_setup):

