from playwright.sync_api import Page

from pages.base_page import BasePage


class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        self.__get_in_touch_message = "//h2[text()='Get In Touch']"
        self.__success_message = ".status.alert.alert-success"
        self.__name_input = "input[data-qa='name']"
        self.__email_input = "input[data-qa='email']"
        self.__subject_input = "input[data-qa='subject']"
        self.__message_input = "textarea[data-qa='message']"
        self.__upload_file_input = "input[name='upload_file']"
        self.__submit_button = "input[type='submit']"

    def send_message(self, name: str, email: str, subject: str, message: str) -> None:
        self.input(self.__name_input, name)
        self.input(self.__email_input, email)
        self.input(self.__subject_input, subject)
        self.input(self.__message_input, message)
        self.set_input_files(self.__upload_file_input, "pytest.ini")
        self.click(self.__submit_button)

    def handle_alert(self) -> None:
        self.page.on("dialog", lambda dialog: dialog.accept())

    def click_submit_btn(self) -> None:
        self.click(self.__submit_button)

    def verify_success_message(self) -> None:
        self.verify(self.__success_message)

    def verify_account_deleted_msg(self) -> None:
        self.verify(self.__get_in_touch_message)
