import logging

def assert_text_in_page(driver, text):
    """Checks if the given text is present in the page source."""
    assert text in driver.page_source, f"'{text}' not found in page source."

def assert_element_exists(driver, locator):
    """Verifies if an element is present."""
    assert driver.find_element(*locator), f"Element {locator} not found."

def log_and_assert(condition, message):
    """Logs the assertion message and checks condition."""
    logging.info(message)
    assert condition, message