from src.pages.common.BaseWrapper import BaseWrapper
from src.pages.webElements.ButtonElement import ButtonElement


class NavigationPage(BaseWrapper):
    """
        Locators and methods for navigation menu.
    """
    NAV_PAGE_TITLE_CSS = "span.nav-item-text"
    NAV_EDIT_PROFILE_CSS = "a:nth-child(1) > button"
    NAV_LOGOUT_CSS = "a:nth-child(2) > button"
    NAV_USER_NAME_CSS = "h4.user-name"

    def __init__(self, driver):
        super().__init__(driver)
        self.navigation_edit_profile_btn = ButtonElement(self.NAV_EDIT_PROFILE_CSS, driver)
        self.log_out_btn = ButtonElement(self.NAV_LOGOUT_CSS, driver)

    def go_to_page(self, page_title):
        """
            Method for click on page depending on page_title value.
            page_title values for admin:
                'Home' - Home page
                'Comuna' - Comuna page
                'Admin' - Admin page
                'Issues' - Issues page
            page_title for user:
                'Home' - Home page
                'Profile' - Profile page
                'Draft' - Drafts page
                'Search Users' - Search/users page
                'Recurrent Events' - eventSchedules page
                'Contact us' - contactAdmin page
                'Comuna' Comuna page
        """

        elements = self.find_elements(self.NAV_PAGE_TITLE_CSS)
        for element in elements:
            if page_title in element.text:
                element.click()
                return

    def get_user_name(self):
        return self.find_element_by_css(self.NAV_USER_NAME_CSS).text
