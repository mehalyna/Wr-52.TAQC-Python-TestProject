"""This module contains tests for the events page of the unauthorized user."""
import allure
import pytest


@allure.parent_suite('Events Page')
@allure.suite('Unauthorized User')
@allure.title("Unauthorized user can't see private events")
@pytest.mark.skip(reason="This test is not implemented yet")
def test_unauthorized_user_can_not_see_private_events() -> None:
    # TODO: implement a test for the events page of the unauthorized user\
    # and check that the private events are not shown
    pass
