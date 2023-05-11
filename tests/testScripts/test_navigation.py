import os
import config


def test_redirect_to_home_page(app):
    """
             Verify that an authorized user can move to the home page from any page of the system
    """
    email = os.getenv("EMAIL7")
    password = os.getenv("PASSWORD7")

    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(email, password)

    app.landing.find_event_btn.click_btn_by_css()
    app.navigation.go_to_page("Profile")
    app.header.event_express_button.click_btn_by_xpath()

    assert app.driver.current_url == f'{config.BASE_URL}home/events'
