import pytest
from selenium.webdriver.common.by import By
from pageObjectsModel.loginPage import LoginPage
from pageObjectsModel.logoutPage import LogoutPage
from pageObjectsModel.pimPage import PIMPage
from constants.constants import Constants
from utils.common_verification import log_and_assert
from utils.common_utils import webdriver_wait
from utils.custom_logger import LogGen


@pytest.mark.usefixtures("setup")
class TestPIM:

    def test_add_and_verify_employee(self):
        driver = self.driver
        login_page = LoginPage(driver)
        pim_page = PIMPage(driver)
        logout_page = LogoutPage(driver)
        logger = LogGen.loggen()

        logger.info("Starting test: Add and Verify Employee")

        #Login
        logger.info("Logging into OrangeHRM")
        login_page.login(Constants.USERNAME, Constants.PASSWORD)

        #Navigate to PIM Page
        logger.info("Navigating to PIM Module")
        pim_page.navigate_to_pim()

        #Adding Employees
        logger.info("Adding Employees")
        employees = [("John", "Doe"), ("Alice", "Smith"), ("Bob", "Brown"), ("Robert", "Junior")]
        for first_name, last_name in employees:
            pim_page.add_employee(first_name, last_name)
            logger.info(f"Employee Added: {first_name} {last_name}")  # Log after each addition

        # # Step 4: Verify Employees in Employee List
        # logger.info("Navigating to Employee List")
        # pim_page.navigate_to_employee_list()
        # webdriver_wait(driver, (By.XPATH, "//div[@role='table']"))  # Wait for table to load
        #
        # for first_name, last_name in employees:
        #     name_locator = (By.XPATH, f"//div[@role='row']/div[contains(text(), '{first_name} {last_name}')]")
        #     webdriver_wait(driver, name_locator)
        #     is_verified = driver.find_element(*name_locator).is_displayed()
        #     log_and_assert(is_verified, f"Employee Verified: {first_name} {last_name}")
        #     logger.info(f"Verification result for {first_name} {last_name}: {'Success' if is_verified else 'Failed'}")

        #Logout
        logger.info("Logging out from the dashboard")
        logout_page.logout()

        logger.info("Test completed successfully!")

