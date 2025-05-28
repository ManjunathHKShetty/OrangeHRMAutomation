from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def webdriver_wait(driver, element_tuple, timeout=10):
    WebDriverWait(driver=driver, timeout=timeout).until(
        EC.visibility_of_element_located(element_tuple))
