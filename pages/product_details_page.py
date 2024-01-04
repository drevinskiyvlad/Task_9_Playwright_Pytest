from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__product_details = ".product-details"
        self.__product_name = "div[class='product-information'] h2"
        self.__product_category = "//p[contains(text(),'Category')]"
        self.__product_price = "div[class='product-information'] span span"
        self.__product_availability = "//b[contains(text(),'Availability')]"
        self.__product_condition = "//b[contains(text(),'Condition')]"
        self.__product_brand = "//b[contains(text(),'Brand')]"

    def verify_page(self) -> None:
        self.verify(self.__product_details)

    def verify_product_information(self) -> None:
        self.verify(self.__product_name)
        self.verify(self.__product_category)
        self.verify(self.__product_price)
        self.verify(self.__product_availability)
        self.verify(self.__product_condition)
        self.verify(self.__product_brand)
