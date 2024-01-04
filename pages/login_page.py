from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__new_user_signup_message = "div[class='signup-form'] h2"
        self.__new_user_login_message = "div[class='login-form'] h2"
        self.__invalid_login_credentials_message = "//p[text()='Your email or password is incorrect!']"
        self.__invalid_signup_credentials_message = "//p[text()='Email Address already exist!']"
        self.__signup_name_input = "input[data-qa='signup-name']"
        self.__signup_email_input = "input[data-qa='signup-email']"
        self.__login_email_input = "input[data-qa='login-email']"
        self.__login_password_input = "input[data-qa='login-password']"
        self.__signup_button = "button[data-qa='signup-button']"
        self.__login_button = "button[data-qa='login-button']"

    def signup(self, name: str, email: str) -> None:
        self.input(self.__signup_name_input, name)
        self.input(self.__signup_email_input, email)
        self.click(self.__signup_button)

    def login(self, email: str, password: str) -> None:
        self.input(self.__login_email_input, email)
        self.input(self.__login_password_input, password)
        self.click(self.__login_button)

    def verify_invalid_login_credentials_msg(self) -> None:
        self.verify(self.__invalid_login_credentials_message)

    def verify_invalid_signup_credentials_msg(self) -> None:
        self.verify(self.__invalid_signup_credentials_message)

    def verify_register(self) -> None:
        self.verify(self.__new_user_signup_message)

    def verify_login(self) -> None:
        self.verify(self.__new_user_login_message)
