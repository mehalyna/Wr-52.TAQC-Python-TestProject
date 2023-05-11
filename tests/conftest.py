# Pytest configuration file
# See https://docs.pytest.org/en/latest/ for more information

import allure
import pytest
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import config
from src.common.BasePage import BasePage


@pytest.fixture(scope="session", autouse=True)
def load_env() -> None:
    load_dotenv()


@pytest.fixture(scope="function")
def app():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield BasePage(driver)
    driver.quit()


@pytest.fixture(scope="function")
def admin_setup(base=app):
    """Login as an admin"""
    base.go_to_site()
    base.landing.sign_up_btn.click_btn_by_css()
    base.modal.login(config.ADMIN_EMAIL, config.ADMIN_PASS)
    return base


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook the "item" object on a test failure"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, base=app):
    """Make screenshot on a test failure"""
    yield
    if request.node.rep_setup.failed:
        make_screenshot(base.driver, request.function.__name__)
    elif request.node.rep_call.failed:
        make_screenshot(base.driver, request.function.__name__)


def make_screenshot(driver, function_name) -> None:
    """Method for making a screenshot."""
    allure.attach(driver.get_screenshot_as_png(),
                  name=function_name,
                  attachment_type=AttachmentType.PNG)
