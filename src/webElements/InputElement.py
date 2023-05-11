from src.common.BaseWrapper import BaseWrapper


class InputElement(BaseWrapper):
    """Class for sending data to input field."""

    def __init__(self, selector, driver) -> None:
        """Method for class fields declaration."""
        super().__init__(driver)
        self.selector = selector

    def send_data_by_css(self, string: str) -> None:
        """Method for sending data to input field by css.
        :param string: Variable string should contain text which we need to enter.
        """
        self.find_element_by_css(self.selector).send_keys(string)

    def send_data_by_xpath(self, string: str) -> None:
        """Method for sending data to input field by xpath.
        :param string: Variable string should contain text which we need to enter.
        """
        self.find_element_by_xpath(self.selector).send_keys(string)

    def clear_field_by_css(self) -> None:
        self.find_element_by_css(self.selector).clear()
