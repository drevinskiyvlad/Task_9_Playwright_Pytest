from playwright.sync_api import Page

from pages.base_page import BasePage


class AllProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__product_list_title = ".title.text-center"
        self.__first_product_details_link = "(//a[contains(text(),'View Product')])[1]"

    def click_first_product_details_link(self) -> None:
        self.click(self.__first_product_details_link)

    def verify_page(self) -> None:
        self.verify(self.__product_list_title)
