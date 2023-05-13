"""Testing the 'Landing' page"""
import os
import re
import time

import allure
import pytest
from allure_commons.types import Severity

import config


@pytest.mark.skip(reason="to be verified")
@allure.title("Test login:")
@allure.severity(Severity.BLOCKER)
def test_landing_login(admin_setup) -> None:
    """Verify that user has the ability to login in as an Admin."""
    expected_result = "AlexTestEngineer"
    admin_setup.landing.find_event_btn.click_btn_by_css()
    assert expected_result == admin_setup.landing_authorized_user.get_user_name(), \
        "username results are not the same as expected"
    with allure.step("Click find event button and go to home page"):
        admin_setup.landing.find_event_btn.click_btn_by_css()
    with allure.step("Verify username is as expected"):
        assert expected_result == admin_setup.landing_authorized_user.get_user_name(), \
            "username results are not the same as expected"


@pytest.mark.skip(reason="to be verified")
def test_landing_registration(app) -> None:
    """Verify that the user has the ability to register a new account."""
    expected_result = "Your registration was successfully. Please confirm your email."
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.registration(config.ADMIN_EMAIL, config.ADMIN_PASS)
    assert expected_result == app.modal.get_success_register_text(), \
        "alert message is not the same as expected"


def test_background_image_changes(app) -> None:
    """Verify that background image changes"""
    app.landing.go_to_site()
    pattern = r"\/([^\/]+\.jpg)"
    time_limit = 15

    # Store initial image filename
    init_image = app.landing.get_background_image().get_attribute('style')
    init_img_filename = re.search(pattern, init_image).group(1)
    while time_limit > 0:
        cur_image = app.landing.get_background_image().get_attribute('style')
        cur_img_filename = re.search(pattern, cur_image).group(1)

        # Compare filenames to make sure they're different
        if cur_img_filename != init_img_filename:
            break
        time_limit -= 1
        time.sleep(1)

    # Verify that the background image changed before the time limit was reached
    assert init_image != cur_image, f"The background image did not change after {time_limit} seconds"


def test_background_image_changes_every_5_seconds(app) -> None:
    """Verify that background image changes every 5 seconds"""
    app.landing.go_to_site()
    pattern = r"\/([^\/]+\.jpg)"
    time_limit = 15

    # Store initial image filename
    init_image = app.landing.get_background_image().get_attribute('style')
    init_img_filename = re.search(pattern, init_image).group(1)
    second_image = None

    # Wait until all background images loaded
    while time_limit > 0:
        cur_image = app.landing.get_background_image().get_attribute('style')
        cur_img_filename = re.search(pattern, cur_image).group(1)

        # Compare filenames to make sure they're different
        if cur_img_filename != init_img_filename:
            second_image = cur_img_filename
            time_limit = 15
            break
        time_limit -= 1
        time.sleep(1)

    # Calculate how long it took to change the background image
    time_passed = 0
    while time_limit > 0:
        cur_image = app.landing.get_background_image().get_attribute('style')
        cur_img_filename = re.search(pattern, cur_image).group(1)

        # Compare filenames to make sure they're different
        if cur_img_filename != second_image:
            break
        time_limit -= 1
        time_passed += 1
        time.sleep(1)

    # Verify that the background image changed before the time limit was reached
    assert time_passed <= 5, f"It took background image to change more than 5 seconds: {time_passed} seconds"


def test_event_express_button_redirects_home(app) -> None:
    """Verify that Event Express logo redirects to home page"""
    app.landing.go_to_site()
    app.landing.event_express_logo.click_btn_by_css()
    assert app.driver.current_url == f'{config.BASE_URL}home/events'


def test_registration_form_appears_after_click(app) -> None:
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    registration_form = app.find_element_by_xpath(app.modal.FORM_PAGE_XPATH)
    assert registration_form


def test_sign_in_with_right_credentials(app) -> None:
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(config.IRINA_EMAIL, config.IRINA_PASSWORD)
    assert config.IRINA_ACCOUNT_NAME == app.navigation.get_user_name()


def test_sign_up_with_incorrect_data(app) -> None:
    invalid_email = "user@gmail.com"
    invalid_password = "mvahr"
    expected_result = "Must be 6 characters or more"
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.registration(invalid_email, invalid_password)
    error_msg = app.modal.find_element_by_xpath(app.modal.UNSUCCESS_PAGE_ALERT_TEXT_XPATH)
    assert error_msg.text == expected_result


def test_user_is_redirected_to_privacy_page_when_privacy_link_clicked(app):
    app.landing.go_to_site()
    app.landing.scroll_down_page()
    app.footer.privacy_link.click_btn_by_xpath()
    expected_result = 'Privacy Policy'
    assert expected_result == app.privacy.get_Privacy_page_heading()


def test_pop_up_menu_appears_when_authorized_user_avatar_is_clicked(app):
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(email, password)
    app.landing_authorized_user.avatar_button.click_btn_by_css()
    assert app.landing_authorized_user.log_out_btn
