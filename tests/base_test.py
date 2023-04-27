import unittest
from selenium import webdriver

from src.resources.locators import LandingPageLocators, HeadersLocators, RegistrationFormLocators
from src.pages.landing_page import MainPage

main_page_elements = LandingPageLocators()
headers_elements = HeadersLocators()
reg_form_elements = RegistrationFormLocators()


class EventExpressPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://eventsexpress-test.azurewebsites.net/landing")
        self.main_page = MainPage(self.driver)

    def test_registration_form_appears_after_click(self):
        self.main_page.click(main_page_elements.BUTTON_SIGN_IN_UP)
        registration_form = self.main_page.get_element_on_page(main_page_elements.REGISTRATION_FORM)
        # verify that the element is present on the page
        self.assertTrue(registration_form.is_displayed())

    def test_sign_in_with_right_credentials(self):
        self.main_page.click(main_page_elements.BUTTON_SIGN_IN_UP)
        self.main_page.enter_text(main_page_elements.FIELD_SIGN_IN_FOR_EMAIL, "irynaqccv@gmail.com")
        self.main_page.enter_text(main_page_elements.FIELD_SIGN_IN_FOR_PASSWORD, "Qwerty_123")
        self.main_page.click(main_page_elements.BUTTON_SIGN_IN)
        account_name = self.main_page.get_element_on_page(headers_elements.ACCOUNT_NAME)
        self.assertTrue("Iryna Melenko" in account_name.text)

    def test_sign_up_with_incorrect_data(self):
        self.main_page.click(main_page_elements.BUTTON_SIGN_IN_UP)
        self.main_page.click(main_page_elements.BUTTON_REGISTER)
        self.main_page.enter_text(reg_form_elements.FIELD_SIGN_UP_FOR_EMAIL, "user@gmail.com")
        self.main_page.enter_text(reg_form_elements.FIELD_SIGN_UP_FOR_PASSWORD, "mvahr")
        self.main_page.enter_text(reg_form_elements.FIELD_SIGN_UP_FOR_REPEAT_PASSWORD, "mvahr")
        self.main_page.click(reg_form_elements.BUTTON_SIGN_UP_CONFIRM)
        error_msg = self.main_page.get_element_on_page(reg_form_elements.WRONG_DATA)
        self.assertTrue("Must be 6 characters or more" in error_msg.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
