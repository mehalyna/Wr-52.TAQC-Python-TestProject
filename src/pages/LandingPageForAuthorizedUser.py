from src.common.BaseWrapper import BaseWrapper
from src.webElements.ButtonElement import ButtonElement


class LandingPageForAuthorizedUser(BaseWrapper):
    """Locators and methods for landing page."""

    USER_NAME_BTN_CSS = "#userNameAlign"
    FIND_EVENT_BTN_CSS = "div.buttons > a"
    CREATE_EVENT_BTN_CSS = "div.buttons > button"
    JOIN_EVENTSEXPRESS_BTN_CSS = "div.text-center > div.d-inline-block > button"
    LOG_OUT_BTN_CSS = "div.text-right > div"
    EXPlORE_MORE_EVENTS_BTN_XPATH = "//a[text()='Explore more events']"

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.sign_up_btn = ButtonElement(self.USER_NAME_BTN_CSS, driver)
        self.find_event_btn = ButtonElement(self.FIND_EVENT_BTN_CSS, driver)
        self.create_event_btn = ButtonElement(self.CREATE_EVENT_BTN_CSS, driver)
        self.join_eventsexpress_btn = ButtonElement(self.JOIN_EVENTSEXPRESS_BTN_CSS, driver)
        self.log_out_btn = ButtonElement(self.LOG_OUT_BTN_CSS, driver)
        self.explore_more_events_btn = ButtonElement(self.EXPlORE_MORE_EVENTS_BTN_XPATH, driver)

    def get_user_name(self):
        return self.find_element_by_css(self.USER_NAME_BTN_CSS).text

    def get_explore_more_events_btn(self):
        return self.find_element_by_xpath(self.EXPlORE_MORE_EVENTS_BTN_XPATH)

    def scroll_to_explore_more_events_btn(self):
        return self.scroll_to_element(self.get_explore_more_events_btn())
