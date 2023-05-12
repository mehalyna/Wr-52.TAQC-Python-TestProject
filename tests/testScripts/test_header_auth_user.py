"""This module contains tests for the header for the authenticated user."""

import allure
import pytest


@allure.parent_suite('Navigation')
@allure.suite('Header for authenticated user')
@allure.title("Test the user can see their username on the header:")
@pytest.mark.skip(reason="Implement header tests")
def test_header_username_visible_for_authenticated_user_on_the_header() -> None:
    # TODO: Implement header tests that the user can see their username on the header.
    pass
