from src.pages.common.BaseWrapper import BaseWrapper
from src.pages.webElements.ButtonElement import ButtonElement


class LandingPageForAuthorizedUser(BaseWrapper):
    """
        Locators and methods for landing page.
    """

    USER_NAME_BTN_CSS = "#userNameAlign"
    FIND_EVENT_BTN_CSS = "div.buttons > a"
    CREATE_EVENT_BTN_CSS = "div.buttons > button"
    JOIN_EVENTSEXPRESS_BTN_CSS = "div.text-center > div.d-inline-block > button"
    LOG_OUT_BTN_CSS = "div.text-right > div"
    EVENT_LOGO_XPATH = "//div[@class='col-12']/img"

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_up_btn = ButtonElement(self.USER_NAME_BTN_CSS, driver)
        self.find_event_btn = ButtonElement(self.FIND_EVENT_BTN_CSS, driver)
        self.create_event_btn = ButtonElement(self.CREATE_EVENT_BTN_CSS, driver)
        self.join_eventsexpress_btn = ButtonElement(self.JOIN_EVENTSEXPRESS_BTN_CSS, driver)
        self.log_out_btn = ButtonElement(self.LOG_OUT_BTN_CSS, driver)

    def get_user_name(self):
        return self.find_element_by_css(self.USER_NAME_BTN_CSS).text

    def get_home_page_url(self):
        return self.get_current_url()

    def get_event_details(self):
        return self.find_element_by_xpath(self.EVENT_LOGO_XPATH)