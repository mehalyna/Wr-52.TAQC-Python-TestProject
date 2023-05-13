"""This module contains the tests for the footer."""

import allure
import pytest


@allure.parent_suite('Navigation')
@allure.suite('Footer')
@allure.title("Test the user can see a link to privacy policy on the footer.")
@pytest.mark.skip(reason="Implement footer tests")
def test_footer_privacy_policy_link_visible_on_page_load() -> None:
    # TODO: Implement footer a test that checks if the user can see a link to privacy policy on the footer.
    pass


@allure.parent_suite('Navigation')
@allure.suite('Footer')
@allure.title("Test the user is redirected to privacy page.")
def test_user_is_redirected_to_privacy_page_when_privacy_link_clicked(app):
    app.landing.go_to_site()
    app.landing.scroll_down_page()
    app.footer.privacy_link.click_btn_by_xpath()
    expected_result = 'Privacy Policy'
    assert expected_result == app.privacy.get_Privacy_page_heading()
