from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """The BasePage class holds all common functionality across the website.
    Also provides a nice wrapper when dealing with selenium functions that may
    not be easy to understand.
    """

    def __init__(self, driver: webdriver):
        """This function is called every time a new object of the base class is created"""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click(self, by_locator):
        """Performs click on web element whose locator is passed to it"""
        custom_button = self.get_element_on_page(by_locator)
        custom_button.click()

    def get_element_on_page(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def enter_text(self, by_locator, text):
        custom_element = self.get_element_on_page(by_locator)
        custom_element.send_keys(text)

    # def get_title(self, title) -> str:
    #     """Returns the title of the page"""
    #     # WebDriverWait(self.driver, 10).until(EC.title_is(title))
    #     return self.driver.title


class Events_page(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)


class HeaderSection(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
