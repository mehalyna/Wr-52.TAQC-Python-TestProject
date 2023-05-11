from src.common.BaseWrapper import BaseWrapper
from src.webElements.ButtonElement import ButtonElement


class LandingPage(BaseWrapper):
    """Locators and methods for landing page."""

    SIGN_IN_UP_BTN_CSS = "#headbtn"
    FIND_EVENT_BTN_CSS = "div.buttons > a"
    CREATE_EVENT_BTN_CSS = "div.buttons > button"
    JOIN_EVENTSEXPRESS_BTN_CSS = "div.text-center > div.d-inline-block > button"
    LOG_OUT_BTN_CSS = "div.text-right > div"
    All_PAGE_CSS = "html"
    UPCOMING_PUBLIC_EVENT = "img[alt~='Event']"
    BACKGROUND_IMAGE_CSS = "article[style~='background-image:']"
    EVENT_EXPRESS_LOGO_CSS = "#EEButton"

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.sign_up_btn = ButtonElement(self.SIGN_IN_UP_BTN_CSS, driver)
        self.find_event_btn = ButtonElement(self.FIND_EVENT_BTN_CSS, driver)
        self.create_event_btn = ButtonElement(self.CREATE_EVENT_BTN_CSS, driver)
        self.join_eventsexpress_btn = ButtonElement(self.JOIN_EVENTSEXPRESS_BTN_CSS, driver)
        self.log_out_btn = ButtonElement(self.LOG_OUT_BTN_CSS, driver)
        self.event_express_logo = ButtonElement(self.EVENT_EXPRESS_LOGO_CSS, driver)

    def scroll_down_page(self):
        return self.scroll_down(self.All_PAGE_CSS)

    def get_upcoming_public_event(self):
        self.scroll_down_page()
        return self.find_element_by_css(self.UPCOMING_PUBLIC_EVENT)

    def get_background_image(self):
        return self.find_element_by_css(self.BACKGROUND_IMAGE_CSS)
