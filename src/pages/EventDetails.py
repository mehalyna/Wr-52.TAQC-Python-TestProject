from src.common.BaseWrapper import BaseWrapper


class EventDetails(BaseWrapper):
    """Event details page"""

    EVENT_PHOTO_XPATH = "//img[contains(@id,'eventFullPhoto')]"
    EVENT_NAME_XPATH = "//span[@class='title']"
    EVENT_DATE_XPATH = "//time/.."
    EVENT_LOCATION_XPATH = "//div[@class='text-block']//div"
    EVENT_DESCRIPTION_XPATH = "//div[contains(@class, 'text-box-big')]"
    JOIN_BUTTON_XPATH = "//button[contains(@class, 'join-leave')]"

    def get_event_name(self):
        return self.find_element_by_xpath(self.EVENT_NAME_XPATH).text

    def get_event_date(self):
        return self.find_element_by_xpath(self.EVENT_DATE_XPATH).text

    def get_event_location(self):
        locations = [item.text for item in self.find_elements_by_xpath(self.EVENT_LOCATION_XPATH) if item.text != '']
        return ', '.join(locations)

    def get_event_description(self):
        return self.find_element_by_xpath(self.EVENT_DESCRIPTION_XPATH).text

    def join_event(self):
        self.find_element_by_xpath(self.JOIN_BUTTON_XPATH).click()
