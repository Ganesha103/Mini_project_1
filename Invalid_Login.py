from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def guvi_invalid_login(login_url, invalid_email, invalid_password, error_message_xpath):
    """
    Automates login with invalid credentials and captures the error message.
    :param login_url: URL of the GUVI login page.
    :param invalid_email: An invalid email address to test.
    :param invalid_password: An invalid password to test.
    :param error_message_xpath: XPath to locate the error message element.
    :return: The error message text if found, or None if not found.
    """
    driver = webdriver.Chrome()
    driver.get(login_url)
    try:
        # Step 1: Navigate to the login page
        driver.get(login_url)

        # Step 2: Input invalid email and password
        email_field = driver.find_element(By.XPATH, "//*[@id='email']")  # Replace with the actual email field locator
        email_field.send_keys(invalid_email)

        password_field = driver.find_element(By.XPATH, "//*[@id='password']")  # Replace with the actual password field locator
        password_field.send_keys(invalid_password)

        # Step 3: Click the login button
        login_button = driver.find_element(By.XPATH, "//*[@id='login-btn']")  # Replace with actual login button XPath
        login_button.click()

        # Wait for the error message to load
        time.sleep(3)  # Adjust the sleep duration or use explicit waits

        # Step 4: Capture the error message text
        try:
            error_message_element = driver.find_element(By.XPATH, "//*[@id='emailgroup']/div")
            error_message = error_message_element.text
            print(f"Error Message Captured: {error_message}")
            return error_message
        except Exception:
            print("Error message not found.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        # Close the browser
        driver.quit()

