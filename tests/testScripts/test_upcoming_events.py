import config
import pytest

"""
    Testing the upcoming public events
"""

def test_upcoming_public_events_guest(app):
    app.landing.go_to_site()
    assert app.landing.get_upcoming_public_event()

def test_upcoming_public_events_after_login(admin_setup):
    assert admin_setup.landing.get_upcoming_public_event()

def test_upcoming_events_details_after_login(admin_setup):
    admin_setup.landing.find_event_btn.click_btn_by_css()
    admin_setup.landing.get_event_details()
    assert admin_setup.landing_authorized_user.get_event_details()

def test_home_page_after_click_join_event_link(admin_setup):
    expected_result = "https://eventsexpress-test.azurewebsites.net/home/events"
    admin_setup.landing.click_join_event_link()
    assert expected_result in admin_setup.landing_authorized_user.get_home_page_url()
