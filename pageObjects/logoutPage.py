from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.logoutLoc import LogoutLoc

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LogoutLoc.profile_dropdown)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LogoutLoc.logout_button)).click()
