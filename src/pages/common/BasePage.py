from src.pages.common.BaseWrapper import BaseWrapper
from src.pages.EventDetails import EventDetails
from src.pages.LandingPage import LandingPage
from src.pages.LandingPageForAuthorizedUser import LandingPageForAuthorizedUser
from src.pages.ModalPage import ModalPage
from src.pages.NavigationForAdmin import NavigationForAdminPanel
from src.pages.NavigationPage import NavigationPage


class BasePage(BaseWrapper):

    def __init__(self, driver):
        """
            Page initialization.
        """
        super().__init__(driver)
        self.landing = LandingPage(driver)
        self.modal = ModalPage(driver)
        self.navigation = NavigationPage(driver)
        self.admin_panel = NavigationForAdminPanel(driver)
        self.landing_authorized_user = LandingPageForAuthorizedUser(driver)
        self.event_details = EventDetails(driver)
