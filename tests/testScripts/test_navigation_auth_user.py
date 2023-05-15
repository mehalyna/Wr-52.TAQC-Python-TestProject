import os

import allure

from config import BASE_URL


@allure.parent_suite('Navigation')
@allure.suite('Navigation for Authorized User')
@allure.title("Test authorized user can move to the home page from any page of the system")
def test_redirects_to_home_page_from_any_page(app) -> None:
    """Verify that an authorized user can move to the home page from any page of the system"""
    email = os.getenv("EMAIL7")
    password = os.getenv("PASSWORD7")

    with allure.step("Sign in"):
        app.landing.go_to_site()
        app.landing.sign_up_btn.click_btn_by_css()
        app.modal.login(email, password)

    with allure.step("Navigate trough the system"):
        app.landing.find_event_btn.click_btn_by_css()
        app.navigation.go_to_page("Profile")
        app.header.event_express_button.click_btn_by_xpath()

    with allure.step("The user is on the home page"):
        assert app.driver.current_url == f'{BASE_URL}home/events'
