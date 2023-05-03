from src.pages.common.BaseWrapper import BaseWrapper
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ButtonElement(BaseWrapper):
    """
        Class for click on Button by xpath and css selector.
    """

    def __init__(self, selector, driver):
        super().__init__(driver)
        self.selector = selector

    def click_btn_by_css(self):
        """
            Method for click on a needed button by css selector.
        """
        button = self.find_element_by_css(self.selector)
        button.click()

    def click_btn_by_xpath(self):
        """
            Method for click on a needed button by xpath selector.
        """
        button = self.find_element_by_xpath(self.selector)
        button.click()

    def hover_and_click_by_css(self, wait_time=10):
        """
            Method for click on a needed button by css selector with hover over the item and wait.
        """
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.selector)))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

    def click_btn_by_index_css(self, index):
        """
        Method for click on a needed button by index and css selector.
        :param index: Variable index should contain number which we need to input.
        """
        button = self.find_element_by_css(self.selector.format(index))
        button.click()

    def click_btn_by_name_by_xpath(self, btn_name):
        """
            Method for click on a needed button by text button and xpath.
        """
        elements = self.find_elements_by_xpath(self.selector)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return
