from src.pages.common.BaseWrapper import BaseWrapper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InputElement(BaseWrapper):
    """
        Class for sending data to input field.
    """

    def __init__(self, selector, driver):
        """
            Method for class fields declaration.
        """
        super().__init__(driver)
        self.selector = selector

    def send_data_by_css(self, string, timeout=10):
        """
        Method for sending data to input field by css.
        :param string: Variable string should contain text which we need to enter.
        """
        self.find_element_by_css(self.selector).send_keys(string)

    def send_data_by_xpath(self, string):
        """
        Method for sending data to input field by xpath.
        :param string: Variable string should contain text which we need to enter.
        """
        self.find_element_by_xpath(self.selector).send_keys(string)

    def clear_field_by_css(self):
        self.find_element_by_css(self.selector).clear()
