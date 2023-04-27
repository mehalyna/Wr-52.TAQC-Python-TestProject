from selenium.webdriver.common.by import By


class LandingPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    BUTTON_CREATE_EVENT = (
        By.CSS_SELECTOR,
        "#root > div > div > article:nth-child(1) > div > div > button",
    )
    BUTTON_REGISTER = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]/div/div/button[2]/span[1]")
    BUTTON_FIND_EVENT = (By.XPATH, r'//*[@id="root"]/div/div/article[1]/div/div/a')
    BUTTON_SIGN_IN_UP = (By.ID, "headbtn")
    BUTTON_WITH_LOGO = (By.ID, "EEButton")
    BUTTON_SIGN_IN = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[3]/div/button[2]/span[1]")
    BUTTON_JOIN_EVENTS_EXPRESS_ = (
        By.XPATH,
        r'//*[@id="root"]/div/div/article[2]/div[3]/div/button',
    )
    EXPLORE_MORE = (By.XPATH, r'//*[@id="root"]/div/div/article[3]/div[1]/div[2]/a')

    FIELD_SIGN_IN_FOR_EMAIL = (By.XPATH, '/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[1]/div/div/input')
    FIELD_SIGN_IN_FOR_PASSWORD = (By.XPATH, r'/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[2]/div/div/input')

    REGISTRATION_FORM = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]")


class HeadersLocators(object):
    ACCOUNT_NAME = (By.XPATH, '//*[@id="userNameAlign"]')


class RegistrationFormLocators(object):
    REGISTRATION_FORM = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]")
    FIELD_SIGN_IN_ENTER_EMAIL = (By.XPATH, '/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[1]/div/div/input')
    FIELD_SIGN_IN_ENTER_PASSWORD = (By.XPATH, '/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[2]/div/div/input')
    FIELD_SIGN_UP_FOR_EMAIL = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[1]/div/div/input")
    FIELD_SIGN_UP_FOR_PASSWORD = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[2]/div/div/input")
    FIELD_SIGN_UP_FOR_REPEAT_PASSWORD = (
    By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[3]/div/div/input")
    WRONG_DATA = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[3]/div/p")
    BUTTON_SIGN_UP_CONFIRM = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[2]/div/form/div[4]/div/button[2]/span[1]")

