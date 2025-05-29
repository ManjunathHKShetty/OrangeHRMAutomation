from selenium.webdriver.common.by import By

class LogoutLoc:
    profile_dropdown = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    logout_button = (By.XPATH, "//a[@href='/web/index.php/auth/logout']")

