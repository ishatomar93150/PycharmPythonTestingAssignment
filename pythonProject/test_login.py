import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture
def browser():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    # Teardown - close the browser
    driver.quit()


def test_login(browser):
    # Open the Amazon website
    browser.get("https://www.amazon.com/")

    # Find the sign-in link and click on it
    sign_in_link = browser.find_element(By.ID, "nav-link-accountList-nav-line-1")
    sign_in_link.click()

    # Find the email field and enter the email address
    email_field = browser.find_element(By.ID, "ap_email")
    email_field.send_keys("hamyahmed007@gmail.com")

    # Find the continue button and click on it
    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()

    # Find the password field and enter the password
    password_field = browser.find_element(By.ID, "ap_password")
    password_field.send_keys("hamy@royal")

    # Find the sign-in button and click on it
    sign_in_button = browser.find_element(By.ID, "signInSubmit")
    sign_in_button.click()

    # Assertion to verify successful login
    assert "Your Orders" in browser.title, "Login was unsuccessful"
