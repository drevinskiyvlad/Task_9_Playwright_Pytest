from playwright.sync_api import Page
from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__account_created_message = "//b[text()='Account Created!']"
        self.__continue_button = "//a[text()='Continue']"

    def click_continue_btn(self) -> None:
        self.click(self.__continue_button)

    def verify_account_created_msg(self) -> None:
        self.verify(self.__account_created_message)
