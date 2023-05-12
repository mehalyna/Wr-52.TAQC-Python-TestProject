from src.common.BaseWrapper import BaseWrapper
from src.webElements.ButtonElement import ButtonElement


class Footer(BaseWrapper):
    """Footer element locators"""

    PRIVACY_LINK_XPATH = "//div[@class='links-to-pages']//a[@href='/privacy']"
    TERMS_LINK_XPATH = "//div[@class='links-to-pages']//a[@href='/terms']"
    ABOUT_LINK_XPATH = "//div[@class='links-to-pages']//a[@href='/about']"
    CONTACT_LINK_XPATH = "//div[@class='links-to-pages']//a[@href='/contactAdmin']"
    FACEBOOK_LINK_XPATH = "//i[contains(@class,'facebook')]/parent::*/@href"
    INSTAGRAM_LINK_XPATH = "//i[contains(@class,'instagram')]/parent::*/@href"
    YOUTUBE_LINK_XPATH = "//i[contains(@class,'youtube')]/parent::*/@href"

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.privacy_link = ButtonElement(self.PRIVACY_LINK_XPATH, driver)
        self.terms_link = ButtonElement(self.TERMS_LINK_XPATH, driver)
        self.about_link = ButtonElement(self.ABOUT_LINK_XPATH, driver)
        self.contact_link = ButtonElement(self.CONTACT_LINK_XPATH, driver)
        self.facebook_link = ButtonElement(self.FACEBOOK_LINK_XPATH, driver)
        self.instagram_link = ButtonElement(self.INSTAGRAM_LINK_XPATH, driver)
        self.youtube_link = ButtonElement(self.YOUTUBE_LINK_XPATH, driver)
