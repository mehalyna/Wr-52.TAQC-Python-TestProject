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
