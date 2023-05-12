from src.common.BaseWrapper import BaseWrapper
from src.webElements.ButtonElement import ButtonElement


class Header(BaseWrapper):
    """Header class"""

    EVENT_EXPRESS_BUTTON_XPATH = "//a[@id='EEButton']"
    SIGN_IN_OUT_BUTTON_XPATH = "//div[@id='headbtn']"
    USER_NAME_XPATH = "//p[@id='userNameAlign']"
    MY_PROFILE_XPATH = "//button[contains(text(), 'my profile')]"
    LOG_OUT_XPATH = "//button[contains(text(), 'log out')]"
    HELP_AND_FEEDBACK_XPATH = "//button[contains(text(), 'help and feedback')]"

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.event_express_button = ButtonElement(self.EVENT_EXPRESS_BUTTON_XPATH, driver)
        self.user_name = ButtonElement(self.USER_NAME_XPATH, driver)
        self.my_profile = ButtonElement(self.MY_PROFILE_XPATH, driver)
        self.log_out = ButtonElement(self.LOG_OUT_XPATH, driver)
        self.help_and_feedback = ButtonElement(self.HELP_AND_FEEDBACK_XPATH, driver)
        self.sign_in_out_button = ButtonElement(self.SIGN_IN_OUT_BUTTON_XPATH, driver)

    def log_out_user(self) -> None:
        """Log out user"""
        self.log_out.click_btn_by_xpath()
