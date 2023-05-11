"""Testing the upcoming public events
    #TODO - upcoming event appears in "Upcoming events" section on landing page before and after login
    #TODO - user can view details of events
    #TODO - after click on "Join event" home page with events appears
"""

def test_upcoming_public_events_before_login(app):
    app.landing.go_to_site()
    assert app.landing.get_upcoming_public_event()

def test_upcoming_public_events_after_login(admin_setup):
    assert admin_setup.landing.get_upcoming_public_event()

def test_upcoming_events_details_after_login(admin_setup):
    admin_setup.landing.find_event_btn.click_btn_by_css()
    admin_setup.landing_authorized_user.open_event_details()
    assert admin_setup.landing_authorized_user.get_event_logo()

def test_home_page_after_click_join_event_link(admin_setup):
    expected_result = "https://eventsexpress-test.azurewebsites.net/home/events"
    admin_setup.landing_authorized_user.wait_explore_more_events_link_clickable()
    admin_setup.landing.join_event_link.click_btn_by_xpath()
    assert expected_result in admin_setup.landing_authorized_user.get_home_page_url()
