"""This module contains tests for the landing page's user interface."""
import re
import time

import allure


@allure.parent_suite('Landing Page')
@allure.suite('User Interface')
@allure.title("Test background image changes:")
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
    with allure.step("Verify that the background image changed before the time limit was reached"):
        assert init_image != cur_image, f"The background image did not change after {time_limit} seconds"

@allure.parent_suite('Landing Page')
@allure.suite('User Interface')
@allure.title("Test background image changes every 5 seconds:")
def test_background_image_changes_every_5_seconds(app) -> None:
    """Verify that background image changes every 5 seconds"""
    app.landing.go_to_site()
    pattern = r"\/([^\/]+\.jpg)"
    time_limit = 15

    # Store initial image filename
    init_image = app.landing.get_background_image().get_attribute('style')
    init_img_filename = re.search(pattern, init_image).group(1)
    second_image = None

    with allure.step("Wait until all background images loaded"):
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

    with allure.step("Calculate how long it took to change the background image"):
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

    with allure.step("Verify that the background image changed before the time limit was reached"):
        assert time_passed <= 5, f"It took background image to change more than 5 seconds: {time_passed} seconds"
