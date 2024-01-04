from playwright.sync_api import Page

from pages.base_page import BasePage


class TestCasesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__list_of_test_cases_message = "//span[contains(text(),'list of test Cases')]"

    def verify_page(self) -> None:
        self.verify(self.__list_of_test_cases_message)
