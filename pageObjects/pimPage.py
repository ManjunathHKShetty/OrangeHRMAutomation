from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.pimLoc import PIMLoc


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

    def verify_employee(self):
        while True:
            for locator in PIMLoc.name_locators:
                try:
                    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
                    if element:
                        return True
                except:
                    pass
            try:
                next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PIMLoc.next_button))
                next_button.click()
            except:
                print("Reached last page. Employee not found!")
                return False
