import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def browser():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # You can replace Chrome with Firefox if needed
    driver.implicitly_wait(10)  # Implicit wait to handle dynamic elements
    yield driver
    # Teardown - close the browser
    driver.quit()


def add_to_cart(browser):
    # Open the Amazon website
    browser.get("https://www.amazon.com/")

    # Find the search input field and enter a product name
    search_input = browser.find_element(By.ID, "twotabsearchtextbox")
    search_input.send_keys("Samsung Galaxy S21")

    # Find and click the search button
    search_button = browser.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    # Wait for search results to load
    time.sleep(2)

    # Find the first search result and click on it to view details
    first_result = browser.find_element(By.XPATH, "//div[@data-index='0']//h2/a")
    first_result.click()

    # Find the "Add to Cart" button and click on it
    add_to_cart_button = browser.find_element(By.ID, "add-to-cart-button")
    add_to_cart_button.click()

    # Assertion to verify that the item was added to the cart successfully
    assert "Added to Cart" in browser.page_source, "Failed to add item to cart"
