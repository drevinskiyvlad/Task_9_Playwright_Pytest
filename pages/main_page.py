import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__slider_carousel = "#slider-carousel"
        self.__login_button = "a[href='/login']"
        self.__logged_in_user_text = "//a[contains(text(), 'Logged in as ')]"
        self.__delete_account_link = "#header a[href='/delete_account']"
        self.__logout_link = "#header a[href='/logout']"
        self.__contact_us_link = "#header a[href='/contact_us']"
        self.__test_cases_link = "#header a[href='/test_cases']"
        self.__products_link = "#header a[href='/products']"
        self.__subscription_title = "//h2[text()='Subscription']"
        self.__subscribe_email_input = "#susbscribe_email"
        self.__subscribe_button = "#subscribe"
        self.__subscribe_success_message = "#success-subscribe"

    def subscribe(self, email: str) -> None:
        with allure.step('Enter email and click Subscribe button'):
            self.input(self.__subscribe_email_input, email)
            self.click(self.__subscribe_button)

    def click_products_link(self) -> None:
        with allure.step('Click on \'Products\' button'):
            self.click(self.__products_link)

    def click_test_cases_link(self) -> None:
        with allure.step('Click on \'Test Cases\' button'):
            self.click(self.__test_cases_link)

    def click_contact_us_link(self) -> None:
        with allure.step('Click on \'Contact Us\' button'):
            self.click(self.__contact_us_link)

    def click_logout_link(self) -> None:
        with allure.step('Click on \'Logout\' button'):
            self.click(self.__logout_link)

    def click_login_link(self) -> None:
        with allure.step('Click on \'Signup / Login\' button'):
            self.click(self.__login_button)

    def click_delete_account_link(self) -> None:
        with allure.step('Click on \'Delete Account\' button'):
            self.click(self.__delete_account_link)

    def verify_subscribe_success_message(self) -> None:
        with allure.step('Verify success message \'You have been successfully subscribed!\' is visible'):
            self.verify(self.__subscribe_success_message)

    def verify_subscription_title(self) -> None:
        with allure.step('Verify text \'SUBSCRIPTION\''):
            self.verify(self.__subscription_title)

    def verify_logged_in_user(self) -> None:
        with allure.step('Verify that \'Logged in as username\' is visible'):
            self.verify(self.__logged_in_user_text)

    def verify_page(self) -> None:
        with allure.step('Verify that home page is visible successfully'):
            self.verify(self.__slider_carousel)
