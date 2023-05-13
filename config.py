"""Test data for initialization, authorization etc."""

from src.resources.random_person import random_person

BASE_URL = "https://eventsexpress-test.azurewebsites.net/"
ADMIN_EMAIL = "anyemail@gmail.com"
ADMIN_PASS = "123456"
LANDING_SIGN_IN_BUTTON = "Sign In"
NEW_EMAIL, NEW_PASS = random_person()
