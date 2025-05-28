from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
        self.add_employee_button = (By.XPATH, "//a[contains(@class, 'oxd-topbar-body-nav-tab-item') and text()='Add Employee']")
        self.first_name = (By.NAME, "firstName")
        self.last_name = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.employee_list_button = (By.XPATH, "//a[normalize-space()='Employee List']")
        self.employee_list_table = (By.XPATH, "//div[@role='table']")
        self.row_locator = (By.XPATH, "//div[@role='rowgroup']/div[@role='row']")

    def navigate_to_pim(self):
        """Clicks on the PIM module before proceeding."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.pim_menu)).click()

    def add_employee(self, first_name, last_name):
        """Navigates to PIM, clicks 'Add Employee', and fills in the details."""
        self.navigate_to_pim()  # First, click PIM
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_employee_button)).click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name)).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.last_name)).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button)).click()

    def navigate_to_employee_list(self):
        """Navigates to Employee List page and ensures the table is visible."""
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.employee_list_button)).click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.employee_list_table))

        # Scroll to the employee list for visibility
        employee_list = self.driver.find_element(*self.employee_list_table)
        self.driver.execute_script("arguments[0].scrollIntoView();", employee_list)

    def capture_employee_list(self):
        """Extracts and verifies employee names from the Employee List."""
        self.navigate_to_employee_list()  # Ensure page is loaded before extracting

        rows = WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(self.row_locator))

        if not rows:
            print("No employees found in the table!")
            return []

        employee_names = [row.text for row in rows]

        print("Captured Employee Names:", employee_names)
        return employee_names