import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Test data
email = "test@example.com"
password = "TestPassword123"


@pytest.fixture(scope="module")
def browser():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # Teardown - Close the browser after tests are done
    driver.quit()


def test_create_new_account(browser):
    # Open Amazon website
    browser.get("https://www.amazon.com/")

    # Click on 'Account & Lists' link to go to the sign-in page
    sign_in_link = browser.find_element_by_id("nav-link-accountList")
    sign_in_link.click()

    # Click on 'Create your Amazon account' button
    create_account_button = browser.find_element_by_id("createAccountSubmit")
    create_account_button.click()

    # Fill in registration form
    name_input = browser.find_element_by_id("ap_customer_name")
    email_input = browser.find_element_by_id("ap_email")
    password_input = browser.find_element_by_id("ap_password")
    reenter_password_input = browser.find_element_by_id("ap_password_check")
    create_account_submit_button = browser.find_element_by_id("continue")

    name_input.send_keys("John Doe")
    email_input.send_keys(email)
    password_input.send_keys(password)
    reenter_password_input.send_keys(password)

    create_account_submit_button.click()

    # Wait for the registration to complete and verify successful registration
    try:
        WebDriverWait(browser, 10).until(EC.url_contains("amazon.com/gp/css/homepage.html"))
        assert "Your Amazon.com" in browser.title
        print("Registration successful.")
    except TimeoutException:
        print("Registration failed.")
        assert False, "Registration failed."


if __name__ == "__main__":
    pytest.main()
