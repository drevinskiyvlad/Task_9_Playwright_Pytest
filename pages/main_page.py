from playwright.sync_api import Page

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__slider_carousel = "#slider-carousel"
        self.__login_button = "a[href='/login']"
        self.__logged_in_user_text = "//a[contains(text(), 'Logged in as ')]"
        self.__delete_account_button = "a[href='/delete_account']"

    def click_login_btn(self) -> None:
        self.click(self.__login_button)

    def click_delete_account_btn(self) -> None:
        self.click(self.__delete_account_button)

    def verify_logged_in_user(self) -> None:
        self.verify(self.__logged_in_user_text)

    def verify_page(self) -> None:
        self.verify(self.__slider_carousel)

    def visit(self) -> None:
        self.navigate("https://automationexercise.com/")
