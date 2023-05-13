"""This module contains tests for the header for the authenticated user."""

import allure


@allure.parent_suite('Navigation')
@allure.suite('Header for authenticated user')
@allure.title("Test the authenticated user can see their username on the header:")
def test_header_username_visible_for_authenticated_user_on_the_header(admin_setup) -> None:
    with allure.step("The username is visible on the header"):
        assert admin_setup.header.get_username() == "AlexTestEngineer"

@allure.parent_suite('Navigation')
@allure.suite('Header for authenticated user')
@allure.title("Test the authenticated user can see the dropdown menu on the header:")
def test_header_dropdown_menu_visible_for_authenticated_user_on_the_header(admin_setup) -> None:
    with allure.step("The dropdown menu is visible when user clicks on their avatar"):
        assert admin_setup.header.dropdown_menu_is_displayed()
