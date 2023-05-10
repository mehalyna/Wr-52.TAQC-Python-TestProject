# It'll be the importing of report tools here
import time

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


def test_appearance_of_login_form_when_join_events_btn_clicked(app):
    app.landing.go_to_site()
    app.landing.scroll_down(app.landing.JOIN_EVENTSEXPRESS_BTN_CSS)
    app.landing.join_eventsexpress_btn.click_btn_by_css()
    expected_result = app.find_element_by_xpath(app.modal.FORM_PAGE_XPATH)
    assert expected_result
    time.sleep(10)


def test_user_is_redirected_to_navigation_page_when_join_event_is_clicked(app):
    app.landing.go_to_site()
    app.landing.scroll_down(app.landing.JOIN_EVENT_CSS)
    app.landing.join_event.click_btn_by_css()
    expected_result = app.navigation.get_navigation_page_title()
    assert expected_result
    time.sleep(10)


def test_user_is_redirected_to_privacy_page_when_privacy_link_clicked(app):
    app.landing.go_to_site()
    app.landing.scroll_down_page()
    app.footer.privacy_link.click_btn_by_css()
    expected_result = 'Privacy Policy'
    assert expected_result == app.privacy.get_privacy_page_heading()
    time.sleep(10)


def test_user_is_redirected_to_terms_page_when_terms_link_clicked(app):
    app.landing.go_to_site()
    app.landing.scroll_down_page()
    app.footer.terms_link.click_btn_by_css()
    expected_result = 'Terms and Conditions ("Terms")'
    assert expected_result == app.terms.get_terms_page_heading()
    time.sleep(10)
