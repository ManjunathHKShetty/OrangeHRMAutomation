from selenium.webdriver.common.by import By

class PIMLoc:
    pim_menu = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
    add_employee_button = (By.XPATH, "//a[contains(@class, 'oxd-topbar-body-nav-tab-item') and text()='Add Employee']")
    first_name = (By.NAME, "firstName")
    last_name = (By.NAME, "lastName")
    save_button = (By.XPATH, "//button[@type='submit']")
    employee_list_button = (By.XPATH, "//a[normalize-space()='Employee List']")
    employee_list_table = (By.XPATH, "//div[@role='table']")
    name_locators = [
        (By.XPATH, "//div[contains(text(),'Charles')]"),
        (By.XPATH, "//div[contains(text(),'Alice')]"),
        (By.XPATH, "//div[contains(text(),'Bob')]"),
        (By.XPATH, "//div[contains(text(),'David')]")
    ]
    next_button = (By.XPATH, "//button[.//i[contains(@class, 'bi-chevron-right')]]")