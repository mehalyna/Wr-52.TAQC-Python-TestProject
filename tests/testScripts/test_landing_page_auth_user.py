"""This module contains tests for the landing page of the authorized user."""
import os

import allure

from config import BASE_URL


@allure.parent_suite('Landing Page')
@allure.suite('Authorized User')
@allure.title("Test authorized user has the ability to explore more events")
def test_auth_user_can_explore_more_events(app) -> None:
    """Verify that the authorized user has the ability to explore more events"""
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    with allure.step("Open the site"):
        app.landing.go_to_site()

    with allure.step("Click on the Sign Up / Sign In button and login"):
        app.landing.sign_up_btn.click_btn_by_css()
        app.modal.login(email, password)

    with allure.step("Click on the Explore More Events button"):
        app.landing_authorized_user.scroll_to_explore_more_events_btn()
        app.landing_authorized_user.explore_more_events_btn.click_btn_by_xpath()

    with allure.step("The user is on the Events page"):
        assert app.navigation.get_nav_page_title()

@allure.parent_suite('Landing Page')
@allure.suite('Authorized User')
@allure.title("Test authorized user can see the upcoming events")
def test_upcoming_public_events_visible_after_login(admin_setup) -> None:
    with allure.step("The upcoming events are visible"):
        assert admin_setup.landing.get_upcoming_public_event()

@allure.parent_suite('Landing Page')
@allure.suite('Authorized User')
@allure.title("Test authorized user can see the upcoming events details")
def test_upcoming_events_details_visible_after_login(admin_setup) -> None:
    with allure.step("Click the 'Find event' button"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
    with allure.step("Open the event details"):
        admin_setup.landing_authorized_user.open_event_details()
    with allure.step("The event details are visible"):
        assert admin_setup.landing_authorized_user.get_event_logo()

@allure.parent_suite('Landing Page')
@allure.suite('Authorized User')
@allure.title("Test authorized user can see public events after clicking join event link")
def test_redirects_home_page_after_click_join_event_link(admin_setup) -> None:
    expected_result = f"{BASE_URL}home/events"
    with allure.step("Click 'Join event' link"):
        admin_setup.landing_authorized_user.wait_explore_more_events_link_clickable()
        admin_setup.landing.join_event_link.click_btn_by_xpath()
    with allure.step("The public events appear"):
        assert expected_result in admin_setup.landing_authorized_user.get_home_page_url()
