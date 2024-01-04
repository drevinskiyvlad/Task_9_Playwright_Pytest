import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__enter_information_message = "//b[text()='Enter Account Information']"
        self.__gender1_radio = "#id_gender1"
        self.__gender2_radio = "#id_gender2"
        self.__password_input = "#password"
        self.__day_select = "#days"
        self.__month_select = "#months"
        self.__year_select = "#years"
        self.__newsletter_checkbox = "#newsletter"
        self.__special_offers_checkbox = "#optin"
        self.__address_firstname_input = "#first_name"
        self.__address_lastname_input = "#last_name"
        self.__address_company_input = "#company"
        self.__address_address1_input = "#address1"
        self.__address_address2_input = "#address2"
        self.__address_country_select = "#country"
        self.__address_state_input = "#state"
        self.__address_city_input = "#city"
        self.__address_zipcode_input = "#zipcode"
        self.__address_mobile_number_input = "#mobile_number"
        self.__create_account_button = "button[data-qa='create-account']"

    def enter_account_information(self,
                                  gender: int,
                                  password: str,
                                  day: str,
                                  month: str,
                                  year: str) -> None:
        with allure.step('Fill details: Title, Name, Email, Password, Date of birth'):
            if gender == 1:
                self.click(self.__gender1_radio)
            if gender == 2:
                self.click(self.__gender2_radio)
            self.input(self.__password_input, password)
            self.select_option(self.__day_select, day)
            self.select_option(self.__month_select, month)
            self.select_option(self.__year_select, year)
            self.check(self.__newsletter_checkbox)
            self.check(self.__special_offers_checkbox)

    def enter_address_information(self,
                                  firstname: str,
                                  lastname: str,
                                  company: str,
                                  address1: str,
                                  address2: str,
                                  country: str,
                                  state: str,
                                  city: str,
                                  zipcode: str,
                                  mobile_number: str) -> None:
        with allure.step('Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number'):
            self.input(self.__address_firstname_input, firstname)
            self.input(self.__address_lastname_input, lastname)
            self.input(self.__address_company_input, company)
            self.input(self.__address_address1_input, address1)
            self.input(self.__address_address2_input, address2)
            self.select_option(self.__address_country_select, country)
            self.input(self.__address_state_input, state)
            self.input(self.__address_city_input, city)
            self.input(self.__address_zipcode_input, zipcode)
            self.input(self.__address_mobile_number_input, mobile_number)

    def click_create_account_btn(self) -> None:
        with allure.step('Click \'Create account\' button'):
            self.click(self.__create_account_button)

    def verify_enter_information_msg(self) -> None:
        with allure.step('Verify that \'ENTER ACCOUNT INFORMATION\' is visible'):
            self.verify(self.__enter_information_message)
