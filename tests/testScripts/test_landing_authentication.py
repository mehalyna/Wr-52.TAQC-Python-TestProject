"""This module contains tests for user authentication at the landing page."""

import os

import allure
from allure_commons.types import Severity


@allure.parent_suite('Landing Page')
@allure.suite('Authentication')
@allure.title("Test login:")
@allure.severity(Severity.BLOCKER)
def test_user_can_login_on_the_landing_page(admin_setup) -> None:
    """Verify that user has the ability to login in as an Admin."""
    expected_result = "AlexTestEngineer"
    admin_setup.landing.find_event_btn.click_btn_by_css()
    assert expected_result == admin_setup.landing_authorized_user.get_user_name(), \
        "username results are not the same as expected"
    with allure.step("Click event express button on the left corner and go to home page"):
        admin_setup.landing.event_express_logo.click_btn_by_css()
    with allure.step("The username is as expected"):
        assert expected_result == admin_setup.landing_authorized_user.get_user_name(), \
            "username results are not the same as expected"

@allure.parent_suite('Landing Page')
@allure.suite('Authentication')
@allure.title("Test sign in with right credentials:")
@allure.severity(Severity.BLOCKER)
def test_sign_in_with_right_credentials(app) -> None:
    with allure.step("Go to site and click sign in/sign up button"):
        app.landing.go_to_site()
        app.landing.sign_up_btn.click_btn_by_css()
    with allure.step("Sign in with right credentials"):
        app.modal.login(os.getenv("IRINA_EMAIL"), os.getenv("IRINA_PASSWORD"))
    with allure.step("The user is logged in"):
        assert os.getenv("IRINA_ACCOUNT_NAME") == app.navigation.get_user_name()
