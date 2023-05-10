# It'll be the importing of report tools here

import config
import pytest
import time

"""
    Testing the 'Landing' page
"""


def test_landing_login_with_correct_credentials(admin_setup):
    """
         Verify that user has the ability to login in as an Admin.
    """
    expected_result = "AlexTestEngineer"
    admin_setup.landing.find_event_btn.click_btn_by_css()
    assert expected_result == admin_setup.landing_authorized_user.get_user_name(), \
        "username results are not the same as expected"
    time.sleep(10)


def test_landing_registration_with_correct_credentials(app):
    """
        Verify that the user has the ability to register a new account.
    """
    expected_result = "Your register was successfull. Please confirm your email."
    app.landing.go_to_site()
    app.landing.sign_in_up_btn.click_btn_by_css()
    app.modal.registration(config.ADMIN_EMAIL, config.ADMIN_PASS)
    assert expected_result == app.modal.get_success_register_text(), \
        "alert message is not the same as expected"


def test_appearance_of_login_form_when_join_events_btn_clicked(app):
    app.landing.go_to_site()
    app.landing.join_eventsexpress_btn.click_btn_by_css()
    expected_result = app.find_element_by_xpath(app.modal.FORM_PAGE_XPATH)
    assert expected_result


def test_user_is_redirected_to_navigation_page_when_join_event_is_clicked(app):
    app.landing.go_to_site()
    app.landing.join_event.click_btn_by_css()
    expected_result = app.navigation.get_navigation_page_title()
    assert expected_result
