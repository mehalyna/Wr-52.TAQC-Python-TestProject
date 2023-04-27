from src.pages.base_page import BasePage
from src.resources.locators import LandingPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = LandingPageLocators()
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.get_element_on_page(*self.locator.BUTTON_WITH_LOGO) else False
