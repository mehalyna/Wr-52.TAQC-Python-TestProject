import time

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
    EXPlORE_MORE_EVENTS_BTN_XPATH = "//a[text()='Explore more events']"
    UPCOMING_EVENT_LINK_XPATH = "//div[@title='Meeting']/a"
    EVENT_LOGO_XPATH = "//img[contains(@id,'eventFullPhoto')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_up_btn = ButtonElement(self.USER_NAME_BTN_CSS, driver)
        self.find_event_btn = ButtonElement(self.FIND_EVENT_BTN_CSS, driver)
        self.create_event_btn = ButtonElement(self.CREATE_EVENT_BTN_CSS, driver)
        self.join_eventsexpress_btn = ButtonElement(self.JOIN_EVENTSEXPRESS_BTN_CSS, driver)
        self.log_out_btn = ButtonElement(self.LOG_OUT_BTN_CSS, driver)
        self.explore_more_events_btn = ButtonElement(self.EXPlORE_MORE_EVENTS_BTN_XPATH, driver)
        self.upcoming_event_link = ButtonElement(self.UPCOMING_EVENT_LINK_XPATH, driver)

    def get_user_name(self):
        return self.find_element_by_css(self.USER_NAME_BTN_CSS).text

    def get_explore_more_events_btn(self):
        return self.find_element_by_xpath(self.EXPlORE_MORE_EVENTS_BTN_XPATH)

    def scroll_to_explore_more_events_btn(self):
        return self.scroll_to_element(self.get_explore_more_events_btn())

    def get_home_page_url(self):
        return self.get_current_url()

    def open_event_details(self):
        return self.upcoming_event_link.click_btn_by_xpath()

    def get_event_logo(self):
        return self.find_element_by_xpath(self.EVENT_LOGO_XPATH)

    def wait_explore_more_events_link_clickable(self):
        #time.sleep(2)
        return self.wait_until_element_clickable(self.EXPlORE_MORE_EVENTS_BTN_XPATH)