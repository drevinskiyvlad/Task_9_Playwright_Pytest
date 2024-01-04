import pytest
from playwright.sync_api import Page

from pages.all_products_page import AllProductsPage
from pages.main_page import MainPage
from pages.product_details_page import ProductDetailsPage
from utils.tools import take_screenshot


class TestProducts:
    @pytest.fixture
    def test_setup(self, new_page: Page):
        self.page = new_page

        self.main_page = MainPage(self.page)
        self.all_products_page = AllProductsPage(self.page)
        self.product_details_page = ProductDetailsPage(self.page)

        self.main_page.verify_page()
        self.main_page.click_products_link()

    def test_all_products_and_product_details(self, test_setup):
        self.all_products_page.verify_page()
        self.all_products_page.click_first_product_details_link()

        self.product_details_page.verify_page()
        self.product_details_page.verify_product_information()

        take_screenshot(self.page, "All Products and Product Details")

    def test_search_product(self, test_setup):
        valid_product_name = "Men Tshirt"

        self.all_products_page.search_product(valid_product_name)

        self.all_products_page.verify_searched_products_title()
        self.all_products_page.verify_first_product()

        take_screenshot(self.page, "Search Product")
