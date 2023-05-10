from src.pages.common.BaseWrapper import BaseWrapper
from src.pages.webElements.ButtonElement import ButtonElement


class FooterPage(BaseWrapper):
    """
    Locators for FooterPage
    """

    PRIVACY_BUTTON_CSS = '.links-to-pages a:nth-child(1)'
    TERMS_BUTTON_CSS = '.links-to-pages a:nth-child(2)'
    ABOUT_BUTTON_CSS = '.links-to-pages a:nth-child(3)'
    CONTACT_US_BUTTON_CSS = '.links-to-pages a:nth-child(4)'

    def __init__(self, driver):
        super().__init__(driver)

        self.privacy_link = ButtonElement(self.PRIVACY_BUTTON_CSS, driver)
        self.terms_link = ButtonElement(self.TERMS_BUTTON_CSS, driver)
        self.about_link = ButtonElement(self.ABOUT_BUTTON_CSS, driver)
        self.contact_us_link = ButtonElement(self.CONTACT_US_BUTTON_CSS, driver)

    def get_privacy_link(self):
        return self.find_element_by_css(self.PRIVACY_BUTTON_CSS)

    def get_terms_link(self):
        return self.find_element_by_css(self.TERMS_BUTTON_CSS)

    def get_about_link(self):
        return self.find_element_by_css(self.ABOUT_BUTTON_CSS)

    def get_contact_us_link(self):
        return self.find_element_by_css(self.CONTACT_US_BUTTON_CSS)
