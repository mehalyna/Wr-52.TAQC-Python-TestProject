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
    expected_result = "InnaName"
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


def test_landing_registeration_with_invalid_password(app):
    """
    verify the user needs to input a certain number of character for a password to be valid
    """
    expected_result = "Must be 6 characters or more"
    app.landing.go_to_site()
    app.landing.sign_in_up_btn.click_btn_by_css()
    app.modal.registration(config.INVALID_REGISTER_EMAIL, config.INVALID_REGISTER_PASSWORD)
    assert expected_result == app.modal.get_error_message_text_when_registering(), \
        "alert message is not the same as expected"
    time.sleep(10)


def test_appearance_of_login_form_when_join_events_btn_clicked(app):
    app.landing.go_to_site()
    app.landing.join_eventsexpress_btn.click_btn_by_css()
    expected_result = app.find_element_by_xpath(app.modal.FORM_PAGE_XPATH)
    assert expected_result


def test_explore_events_redirects_to_events_page(app):
    app.landing.go_to_site()
    app.landing.explore_more_events.click_btn_by_css()
    expected_result = config.EVENTS_PAGE_URL
    assert expected_result


def test_join_event_button(app):
    app.landing.go_to_site()
    app.landing.join_event.click_btn_by_css()
    expected_result = config.JOIN_EVENT_URL
    assert expected_result


def test_privacy_link_redirects_user_to_privacy_page(app):
    app.landing.go_to_site()
    app.landing.privacy_link.click_btn_by_css()
    expected_result = config.PRIVACY_PAGE_URL
    assert expected_result


def test_terms_link_redirects_user_to_terms_page(app):
    app.landing.go_to_site()
    app.landing.terms_link.click_btn_by_css()
    expected_result = config.TERMS_PAGE_URL
    assert expected_result
    time.sleep(10)


def test_about_link_redirects_user_to_about_page(app):
    app.landing.go_to_site()
    app.landing.about_link.click_btn_by_css()
    expected_result = config.ABOUT_PAGE_URL
    assert expected_result
    time.sleep(10)


def test_contact_link_redirects_user_to_contact_us_page(app):
    app.landing.go_to_site()
    app.landing.contact_us_link.click_btn_by_css()
    expected_result = config.CONTACT_US_PAGE
    assert expected_result
    time.sleep(10)
