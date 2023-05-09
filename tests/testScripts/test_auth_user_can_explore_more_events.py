import os


def test_auth_user_can_explore_more_events(app):
    """
             Verify that the authorized user has the ability to explore more events
    """
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(email, password)
    app.landing_authorized_user.scroll_to_explore_more_events_btn()
    app.landing_authorized_user.explore_more_events_btn.click_btn_by_xpath()
    assert app.navigation.get_nav_page_title()



