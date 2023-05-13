from src.common.BaseWrapper import BaseWrapper


class Privacy_Page(BaseWrapper):
    """privacy page locators"""
    PRIVACY_HEADING_CSS = '.privacy h1'

    def get_Privacy_page_heading(self):
        return self.find_element_by_css(self.PRIVACY_HEADING_CSS).text
