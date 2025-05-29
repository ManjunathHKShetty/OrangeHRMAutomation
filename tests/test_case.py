import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.logoutPage import LogoutPage
from pageObjects.pimPage import PIMPage
from constants.constants import Constants
from utils.custom_logger import LogGen


@pytest.mark.usefixtures("setup")
class TestPIM:

    def test_login_add_and_verify_employee(self):
        driver = self.driver
        login_page = LoginPage(driver)
        pim_page = PIMPage(driver)
        logout_page = LogoutPage(driver)
        logger = LogGen.loggen()

        logger.info("Starting test: Add and Verify Employee")

        # Login
        logger.info("Logging into OrangeHRM")
        login_page.login(Constants.USERNAME, Constants.PASSWORD)

        # Navigate to PIM Page
        logger.info("Navigating to PIM Module")
        pim_page.navigate_to_pim()

        # Add Employees
        employees = [("Charles", "Doe"), ("Alice", "Smith"), ("Bob", "Brown"), ("David", "Junior")]
        for first_name, last_name in employees:
            pim_page.add_employee(first_name, last_name)
            logger.info(f"Employee Added: {first_name} {last_name}")

        # Verify Employees in Employee List
        logger.info("Navigating to Employee List")
        pim_page.navigate_to_employee_list()

        for first_name, last_name in employees:
            is_found = pim_page.verify_employee()
            assert is_found, f"Name Verified: {first_name}"
            logger.info(f"Name Verified: {first_name} {last_name}")

        logger.info("Employee verification successful")

        # Logout
        logger.info("Logging out from the dashboard")
        logout_page.logout()

        logger.info("Test completed successfully!")