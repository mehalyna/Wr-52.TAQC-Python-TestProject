"""This module contains tests for the landing page of the unauthorized user."""

import allure

import config


@allure.parent_suite('Landing Page')
@allure.suite('Unauthorized User')
@allure.title("Test registration for a new user:")
def test_landing_a_new_user_can_register(app) -> None:
    """Verify that the user has the ability to register a new account."""
    expected_result = "Your register was successfull. Please confirm your email."
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.registration(config.NEW_EMAIL, config.NEW_PASS)
    assert expected_result == app.modal.get_success_register_text(), \
        "alert message is not the same as expected"

@allure.parent_suite('Landing Page')
@allure.suite('Unauthorized User')
@allure.title("Test registration form appears after click:")
def test_registration_form_appears_after_click(app) -> None:
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    registration_form = app.find_element_by_xpath(app.modal.FORM_PAGE_XPATH)
    with allure.step("Verify that registration form appeared"):
        assert registration_form

@allure.parent_suite('Landing Page')
@allure.suite('Unauthorized User')
@allure.title("Test can not sign in with incorrect credentials:")
def test_sign_up_with_incorrect_data_fails(app) -> None:
    invalid_email = "user@gmail.com"
    invalid_password = "mvahr"
    expected_result = "Must be 6 characters or more"
    with allure.step("Go to site and click sign in/sign up button"):
        app.landing.go_to_site()
        app.landing.sign_up_btn.click_btn_by_css()
    with allure.step("Sign in with incorrect credentials"):
        app.modal.registration(invalid_email, invalid_password)
    with allure.step("Verify that error message is as expected"):
        error_msg = app.modal.find_element_by_xpath(app.modal.UNSUCCESS_PAGE_ALERT_TEXT_XPATH)
        assert error_msg.text == expected_result

@allure.parent_suite('Landing Page')
@allure.suite('Unauthorized User')
@allure.title("Test user can see public events before login")
def test_upcoming_public_events_visible_before_login(app) -> None:
    app.landing.go_to_site()
    with allure.step("Check that the public event appears"):
        assert app.landing.get_upcoming_public_event()

@allure.parent_suite('Landing Page')
@allure.suite('Unauthorized User')
@allure.title("Test user can see public events after clicking join event link")
def test_redirects_home_page_after_click_join_event_link(app) -> None:
    expected_result = "https://eventsexpress-test.azurewebsites.net/home/events"
    app.landing.go_to_site()
    app.landing_authorized_user.wait_explore_more_events_link_clickable()
    app.landing.join_event_link.click_btn_by_xpath()
    assert expected_result in app.landing_authorized_user.get_home_page_url()
