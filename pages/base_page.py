from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get(self, locator: str):
        return self.page.locator(locator)

    def click(self, locator: str):
        self.page.wait_for_selector(locator, state="visible")
        self.get(locator).click()

    def check(self, locator: str):
        self.get(locator).check()

    def select_option(self, locator: str, option:str):
        self.get(locator).select_option(option)

    def set_input_files(self, locator: str, files: str):
        self.get(locator).set_input_files(files)

    def input(self, locator: str, text: str):
        self.get(locator).fill(text)

    def verify(self, locator: str):
        expect(self.get(locator)).to_be_visible()
