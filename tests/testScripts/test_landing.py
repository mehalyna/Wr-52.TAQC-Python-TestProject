# It'll be the importing of report tools here

import re
import time

import pytest

import config

"""
    Testing the 'Landing' page
"""

@pytest.mark.skip(reason="to be verified")
def test_landing_login(admin_setup):
    """
         Verify that user has the ability to login in as an Admin.
    """
    expected_result = "AlexTestEngineer"
    admin_setup.landing.find_event_btn.click_btn_by_css()
    assert expected_result == admin_setup.landing_authorized_user.get_user_name(), \
        "username results are not the same as expected"

@pytest.mark.skip(reason="to be verified")
def test_landing_registration(app):
    """
        Verify that the user has the ability to register a new account.
    """
    expected_result = "Your registration was successfully. Please confirm your email."
    app.landing.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.registration(config.ADMIN_EMAIL, config.ADMIN_PASS)
    assert expected_result == app.modal.get_success_register_text(), \
        "alert message is not the same as expected"

def test_background_image_changes(app):
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

def test_background_image_changes_every_5_seconds(app):
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

def test_event_express_button_redirects_home(app):
    """Verify that Event Express logo redirects to home page"""
    app.landing.go_to_site()
    app.landing.event_express_logo.click_btn_by_css()
    assert app.driver.current_url == f'{config.BASE_URL}home/events'
