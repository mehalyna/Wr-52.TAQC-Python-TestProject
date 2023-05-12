"""This module contains tests for the header for the unauthenticated user."""

import allure

from config import BASE_URL


@allure.parent_suite('Navigation')
@allure.suite('Header for unauthenticated user')
@allure.title("Test event express logo redirects to home page:")
def test_event_express_button_redirects_home(app) -> None:
    """Verify that Event Express logo redirects to home page"""
    app.landing.go_to_site()
    app.landing.event_express_logo.click_btn_by_css()
    with allure.step("Verify that the current url is equal to the events page url"):
        assert app.driver.current_url == f'{BASE_URL}home/events'
