import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class AllProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__product_list_title = "div.features_items .title.text-center"
        self.__first_product = "(//div[@class='col-sm-4'])[2]"
        self.__first_product_details_link = "(//a[contains(text(),'View Product')])[1]"
        self.__search_input = "#search_product"
        self.__search_button = "#submit_search"
        self.__searched_products_title = "//h2[text()='Searched Products']"

    def search_product(self, product_name: str) -> None:
        with allure.step('Enter product name in search input and click search button'):
            self.input(self.__search_input, product_name)
            self.click(self.__search_button)

    def click_first_product_details_link(self) -> None:
        with allure.step('Click on \'View Product\' of first product'):
            self.click(self.__first_product_details_link)

    def verify_products(self) -> None:
        with allure.step('Verify all the products related to search are visible'):
            self.verify(self.__first_product)

    def verify_searched_products_title(self) -> None:
        with allure.step('Verify \'SEARCHED PRODUCTS\' is visible'):
            self.verify(self.__searched_products_title)

    def verify_page(self) -> None:
        with allure.step('Verify user is navigated to ALL PRODUCTS page successfully'):
            self.verify(self.__product_list_title)
