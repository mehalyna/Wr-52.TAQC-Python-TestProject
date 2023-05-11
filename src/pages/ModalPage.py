from src.pages.common.BaseWrapper import BaseWrapper
from src.pages.webElements.ButtonElement import ButtonElement
from src.pages.webElements.InputElement import InputElement

SIGN_IN_BUTTON_TEXT = "SIGN IN"
FORM_PAGE_LOGIN_TEXT = "LOGIN"
FORM_PAGE_REGISTER_TEXT = "REGISTER"
FORM_PAGE_BUTTON_SING_UP_TEXT = "SIGN UP"


class ModalPage(BaseWrapper):
    """
        Locators and methods for Modal page.
    """
    MODAL_DIALOG_XPATH = "//div[@class='MuiDialog-root'][2]"
    FORM_PAGE_XPATH = f"{MODAL_DIALOG_XPATH}//span[@class='MuiTab-wrapper']"
    FORM_EMAIL_INP_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='email']"
    FORM_PASSWORD_INP_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='password']"
    FORM_REGISTER_PASSWORD_REPEAT_INP_XPATH = f"{MODAL_DIALOG_XPATH}//input[@name='RepeatPassword']"
    FORM_BTN_XPATH = f"{MODAL_DIALOG_XPATH}//span[@class='MuiButton-label']"
    SUCCESS_PAGE_ALERT_TEXT_CSS = "div.alert-success"
    UNSUCCESS_PAGE_ALERT_TEXT_XPATH = "//input[@name='password']/parent::*/following-sibling::p[contains(@class, " \
                                      "'Mui-error')] "

    def __init__(self, driver):
        super().__init__(driver)
        self.email_inp = InputElement(self.FORM_EMAIL_INP_XPATH, driver)
        self.pass_inp = InputElement(self.FORM_PASSWORD_INP_XPATH, driver)
        self.pass_repeat_inp = InputElement(self.FORM_REGISTER_PASSWORD_REPEAT_INP_XPATH, driver)
        self.sign_in_up_clear_btns = ButtonElement(self.FORM_BTN_XPATH, driver)
        self.page_btns = ButtonElement(self.FORM_PAGE_XPATH, driver)

    def get_success_register_text(self):
        """
            Method for getting the message about successful registration.
        """
        return self.find_element_by_css(self.SUCCESS_PAGE_ALERT_TEXT_CSS).text

    def login(self, username, password):
        """
        Sign in method as a scenario
        actor - is a person with own permissions (admin or user).
        :param username: username
        :param password: pass phrase
        """
        self.email_inp.send_data_by_xpath(username)
        self.pass_inp.send_data_by_xpath(password)
        self.sign_in_up_clear_btns.click_btn_by_name_by_xpath(SIGN_IN_BUTTON_TEXT)

    def registration(self, username, password):
        """
        Registration method as a scenario
        actor - is a person with own permissions (admin or user).
        :param username: username
        :param password: pass phrase
        """
        self.page_btns.click_btn_by_name_by_xpath(FORM_PAGE_REGISTER_TEXT)
        self.email_inp.send_data_by_xpath(username)
        self.pass_inp.send_data_by_xpath(password)
        self.pass_repeat_inp.send_data_by_xpath(password)
        self.sign_in_up_clear_btns.click_btn_by_name_by_xpath(FORM_PAGE_BUTTON_SING_UP_TEXT)

    def get_modal_dialog(self):
        return self.find_element_by_xpath(self.MODAL_DIALOG_XPATH)
