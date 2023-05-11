from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.common.BaseWrapper import BaseWrapper


class NavigationForAdminPanel(BaseWrapper):
    """Locators and methods for navigation menu on admin panel"""

    ADMIN_MENU = "#sub-nav"
    USER_NAME = "h4.user-name"

    def go_to_page(self, page_title, wait_time=10):
        """Method for click on page depending on page_title value.
            Pages of Admin Panel:
                "Categories" - Edit_category
                "UnitsOfMeasuring" - Units_of_measuring
                "Users" - User
                "Notification Templates" - NotificationPage
                "Tracks" - Track
        """
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.ADMIN_MENU)))
        elements = self.find_elements(self.ADMIN_MENU)
        for element in elements:
            if page_title in element.text:
                element.click()
                return
