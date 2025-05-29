from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.loginLoc import LoginLoc
from utils.common_utils import webdriver_wait
from constants.constants import Constants

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.get(Constants.ORANGEHRM_URL)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginLoc.username)).send_keys(username)
        self.driver.find_element(*LoginLoc.password).send_keys(password)
        self.driver.find_element(*LoginLoc.login_button).click()
        webdriver_wait(self.driver, (By.XPATH, "//h6[text()='Dashboard']"))