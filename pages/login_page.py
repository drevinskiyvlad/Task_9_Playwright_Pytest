from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__new_user_signup_message = "div[class='signup-form'] h2"
        self.__new_user_login_message = "div[class='login-form'] h2"
        self.__name_input = "input[data-qa='signup-name']"
        self.__email_input = "input[data-qa='signup-email']"
        self.__signup_button = "button[data-qa='signup-button']"

    def signup(self, name: str, email: str) -> None:
        self.input(self.__name_input, name)
        self.input(self.__email_input, email)
        self.click(self.__signup_button)

    def verify_register(self) -> None:
        self.verify(self.__new_user_signup_message)

    def verify_login(self) -> None:
        self.verify(self.__new_user_login_message)
