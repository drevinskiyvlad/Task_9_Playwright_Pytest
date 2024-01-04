from playwright.sync_api import Page

from pages.base_page import BasePage


class AllProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__product_list_title = ".title.text-center"
        self.__first_product = "(//div[@class='col-sm-4'])[2]"
        self.__first_product_details_link = "(//a[contains(text(),'View Product')])[1]"
        self.__search_input = "#search_product"
        self.__search_button = "#submit_search"
        self.__searched_products_title = "//h2[text()='Searched Products']"

    def search_product(self, product_name: str) -> None:
        self.input(self.__search_input, product_name)
        self.click(self.__search_button)

    def click_first_product_details_link(self) -> None:
        self.click(self.__first_product_details_link)

    def verify_first_product(self) -> None:
        self.verify(self.__first_product)

    def verify_searched_products_title(self) -> None:
        self.verify(self.__searched_products_title)

    def verify_page(self) -> None:
        self.verify(self.__product_list_title)
