import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # You can replace Chrome with Firefox if needed
    driver.implicitly_wait(10)  # Implicit wait to handle dynamic elements
    yield driver
    # Teardown - close the browser
    driver.quit()


def test_search_product(browser):
    # Open the Amazon website
    browser.get("https://www.amazon.com/")

    # Find the search input field and enter a product name
    search_input = browser.find_element(By.ID, "twotabsearchtextbox")
    search_input.send_keys("Samsung Galaxy S21")  # Change the product name as needed

    # Find and click the search button
    search_button = browser.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    # Assertion to verify that search results are displayed
    assert "Samsung Galaxy S21" in browser.title, "Search results not displayed"
