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

    def click_products_btn(self) -> None:
        self.click(self.__products_link)

    def click_test_cases_btn(self) -> None:
        self.click(self.__test_cases_link)

    def click_contact_us_btn(self) -> None:
        self.click(self.__contact_us_link)

    def click_logout_btn(self) -> None:
        self.click(self.__logout_link)

    def click_login_btn(self) -> None:
        self.click(self.__login_button)

    def click_delete_account_btn(self) -> None:
        self.click(self.__delete_account_link)

    def verify_logged_in_user(self) -> None:
        self.verify(self.__logged_in_user_text)

    def verify_page(self) -> None:
        self.verify(self.__slider_carousel)

    def visit(self) -> None:
        self.navigate("https://automationexercise.com/")
