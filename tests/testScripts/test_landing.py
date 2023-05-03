# It'll be the importing of report tools here

import config
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
