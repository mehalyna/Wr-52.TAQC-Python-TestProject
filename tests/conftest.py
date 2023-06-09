# Pytest configuration file
# See https://docs.pytest.org/en/latest/ for more information

import os

import allure
import pytest
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.common.BasePage import BasePage


@pytest.fixture(scope="session", autouse=True)
def load_env() -> None:
    load_dotenv()

@pytest.fixture(scope="function", name="app")
def main_app():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield BasePage(driver)
    driver.quit()

@pytest.fixture(scope="function")
def admin_setup(app):
    """Login as an admin"""
    app.go_to_site()
    app.landing.sign_up_btn.click_btn_by_css()
    app.modal.login(os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASS"))
    return app

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook the "item" object on a test failure"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, app):
    """Make screenshot on a test failure"""
    yield
    if request.node.rep_setup.failed:
        make_screenshot(app.driver, request.function.__name__)
    elif request.node.rep_call.failed:
        make_screenshot(app.driver, request.function.__name__)

def make_screenshot(driver, function_name) -> None:
    """Method for making a screenshot."""
    allure.attach(driver.get_screenshot_as_png(),
                  name=function_name,
                  attachment_type=AttachmentType.PNG)
