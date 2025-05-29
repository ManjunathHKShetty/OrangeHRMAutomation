from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.logoutLoc import LogoutLoc



class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LogoutLoc.profile_dropdown)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LogoutLoc.logout_button)).click()

class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_pim(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PIMLoc.pim_menu)).click()

    def add_employee(self, first_name, last_name):
        self.navigate_to_pim()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PIMLoc.add_employee_button)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PIMLoc.first_name)).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PIMLoc.last_name)).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PIMLoc.save_button)).click()

    def navigate_to_employee_list(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PIMLoc.employee_list_button)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PIMLoc.employee_list_table))

    def verify_employee(self, first_name, last_name):
        """Scrolls through paginated table and verifies if the employee exists."""
        while True:
            name_locator = (By.XPATH, f"//div[@role='row']/div[contains(text(), '{first_name} {last_name}')]")
            try:
                if WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(name_locator)):
                    print(f"Name Found: {first_name} {last_name}")
                    return True
            except:
                pass

            try:
                next_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(PIMLoc.next_button))
                next_button.click()
            except:
                print(f"Reached last page. {first_name} {last_name} not found!")
                return False