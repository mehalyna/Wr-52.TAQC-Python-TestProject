# It'll be the importing of report tools here

import config
import time
import pytest

"""
    Testing the 'Landing' page
"""


def test_landing_login(admin_setup):
    """
         Verify that user has the ability to login in as an Admin.
    """
    expected_result = "AlexTestEngineer"
    admin_setup.landing.find_event_btn.click_btn_by_css()
    assert expected_result == admin_setup.landing_authorized_user.get_user_name(), \
        "username results are not the same as expected"


def test_landing_registration(app):
    """
        Verify that the user has the ability to register a new account.
    """
    expected_result = "Your registration was successfully. Please confirm your email."
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.registration(config.ADMIN_EMAIL, config.ADMIN_PASS)
    assert expected_result == app.modal.get_success_register_text(), \
        "alert message is not the same as expected"


def test_registration_form_appears_after_click(app):
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    registration_form = app.find_element_by_xpath(app.modal.FORM_PAGE_XPATH)
    assert registration_form


def test_sign_in_with_right_credentials(app):
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.IRINA_EMAIL, config.IRINA_PASSWORD)
    assert config.IRINA_ACCOUNT_NAME == app.navigation.get_user_name()


def test_sign_up_with_incorrect_data(app):
    expected_result = "Must be 6 characters or more"
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.registration(config.INVALID_EMAIL, config.INVALID_PASSWORD)
    error_msg = app.modal.find_element_by_xpath(app.modal.UNSUCCESS_PAGE_ALERT_TEXT_XPATH)
    assert error_msg.text == expected_result
