from src.common.BaseWrapper import BaseWrapper
from src.webElements.ButtonElement import ButtonElement


class Privacy_Page(BaseWrapper):
    """
    privacy page locators
    """
    PRIVACY_HEADING_CSS = '#main > div > h1'

    def __init__(self, driver):
        super().__init__(driver)

    def get_Privacy_page_heading(self):
        return self.find_element_by_css(self.PRIVACY_HEADING_CSS).text


