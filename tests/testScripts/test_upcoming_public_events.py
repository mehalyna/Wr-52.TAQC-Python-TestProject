import config
import pytest



"""
    Testing the upcoming public events
"""

def test_upcoming_public_events_guest(app):
    app.landing.go_to_site()
    assert app.landing.get_upcoming_public_event()


def test_upcoming_public_events_after_login(app, admin_setup):
    assert admin_setup.landing.get_upcoming_public_event()

