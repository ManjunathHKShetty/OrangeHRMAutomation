from selenium.webdriver.common.by import By

class LoginLoc:
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")