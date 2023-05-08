from src.pages.common.BaseWrapper import BaseWrapper
from src.pages.webElements.ButtonElement import ButtonElement


class LandingPage(BaseWrapper):
    """
        Locators and methods for landing page.
    """

    SIGN_IN_UP_BTN_CSS = "#headbtn"
    FIND_EVENT_BTN_CSS = "div.buttons > a"
    CREATE_EVENT_BTN_CSS = "div.buttons > button"
    JOIN_EVENTSEXPRESS_BTN_CSS = "div.text-center > div.d-inline-block > button"
    LOG_OUT_BTN_CSS = "div.text-right > div"
    EXPLORE_MORE_EVENTS_BTN_CSS = '#root > div > div > article.events-article > div.row > div.col-md-2 > a'
    JOIN_EVENT_CSS = '#root > div > div > article.events-article > div.carousel-wrapper.text-center > div > div > div > div > div > div > div > div:nth-child(2) > a'
    PRIVACY_BUTTON_CSS = '#root > div > footer > div.links-to-pages > a:nth-child(1)'
    TERMS_BUTTON_CSS = '#root > div > footer > div.links-to-pages > a:nth-child(2)'
    ABOUT_BUTTON_CSS = '#root > div > footer > div.links-to-pages > a:nth-child(3)'
    CONTACT_US_BUTTON_CSS = '#root > div > footer > div.links-to-pages > a:nth-child(4)'

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_up_btn = ButtonElement(self.SIGN_IN_UP_BTN_CSS, driver)
        self.find_event_btn = ButtonElement(self.FIND_EVENT_BTN_CSS, driver)
        self.create_event_btn = ButtonElement(self.CREATE_EVENT_BTN_CSS, driver)
        self.join_eventsexpress_btn = ButtonElement(self.JOIN_EVENTSEXPRESS_BTN_CSS, driver)
        self.log_out_btn = ButtonElement(self.LOG_OUT_BTN_CSS, driver)
        self.explore_more_events = ButtonElement(self.EXPLORE_MORE_EVENTS_BTN_CSS, driver)
        self.join_event = ButtonElement(self.JOIN_EVENT_CSS, driver)
        self.privacy_link = ButtonElement(self.PRIVACY_BUTTON_CSS, driver)
        self.terms_link = ButtonElement(self.TERMS_BUTTON_CSS, driver)
        self.about_link = ButtonElement(self.ABOUT_BUTTON_CSS, driver)
        self.contact_us_link = ButtonElement(self.CONTACT_US_BUTTON_CSS, driver)

    def get_join_events_express(self):
        return self.find_element_by_css(self.JOIN_EVENTSEXPRESS_BTN_CSS)

    def get_join_event(self):
        return self.find_element_by_css(self.JOIN_EVENT_CSS)

    def get_privacy_link(self):
        return self.find_element_by_css(self.PRIVACY_BUTTON_CSS)

    def get_terms_link(self):
        return self.find_element_by_css(self.TERMS_BUTTON_CSS)

    def get_about_link(self):
        return  self.find_element_by_css(self.ABOUT_BUTTON_CSS)

    def get_contact_us_link(self):
        return self.find_element_by_css(self.CONTACT_US_BUTTON_CSS)
