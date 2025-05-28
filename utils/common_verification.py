import logging

def assert_text_in_page(driver, text):
    assert text in driver.page_source, f"'{text}' not found in page source."

def assert_element_exists(driver, locator):
    assert driver.find_element(*locator), f"Element {locator} not found."

def log_and_assert(condition, message):
    logging.info(message)
    assert condition, message