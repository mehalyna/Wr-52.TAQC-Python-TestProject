from src.pages.common.BaseWrapper import BaseWrapper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class LinkElement(BaseWrapper):
    """
        Class for click on Button by xpath and css selector.
    """

    def __init__(self, selector, driver):
        super().__init__(driver)
        self.selector = selector

    def click_link_by_css(self):
        """
            Method for click on a needed button by css selector.
        """
        link = self.find_element_by_css(self.selector)
        link.click()

    def click_link_by_xpath(self):
        """
            Method for click on a needed button by xpath selector.
        """
        link = self.find_element_by_xpath(self.selector)
        link.click()