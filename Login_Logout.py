from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def guvi_login_logout(login_url, email, password, expected_logout_url,expected_url):
    """
    Automates login and logout process for GUVI and verifies both.
    :param login_url: URL of the GUVI login page.
    :param email: Valid email for login.
    :param password: Valid password for login.
    :param logout_button_xpath: XPath to locate the logout button.
    :param expected_logout_url: URL to validate successful logout.
    :return: Dictionary with login and logout results.
    """
    driver = webdriver.Chrome()
    results = {"login_successful": False, "logout_successful": False}
    try:
        # Step 1: Navigate to the login page
        driver.get(login_url)

        # Step 2: Input valid email and password
        email_field = driver.find_element(By.XPATH, "//*[@id='email']")  # Replace with the actual email field locator
        email_field.send_keys(email)

        password_field = driver.find_element(By.XPATH, "//*[@id='password']")   # Replace with the actual password field locator
        password_field.send_keys(password)

        # Step 3: Click the login button
        login_button = driver.find_element(By.XPATH, "//*[@id='login-btn']")  # Replace with actual login button XPath
        login_button.click()

        # Wait for the page to load after login
        time.sleep(5)  # Adjust based on page load time or use explicit waits

        # Verify successful login by checking the redirected URL
        current_url = driver.current_url
        if current_url == expected_url:
            print("Test Passed: Login was successful.")
            results["login_successful"] = True
        else:
            print(f"Test Failed: Login was not successful. Current URL: {current_url}")
            return results

        # Step 4: Locate and click the logout button
        logout_button_1 = driver.find_element(By.XPATH,"//*[@id = 'dropdown_title']")  # Replace with actual XPath for logout button
        logout_button_1.click()

        logout_button = driver.find_element(By.XPATH,"//div[text()='Sign Out']")  # Replace with actual XPath for logout button
        logout_button.click()


        # Wait for the page to redirect after logout
        time.sleep(9)

        # Verify successful logout by checking the redirected URL
        current_url = driver.current_url
        if current_url == expected_logout_url:
            print("Test Passed: Logout was successful.")
            results["logout_successful"] = True
        else:
            print(f"Test Failed: Logout was not successful. Current URL: {current_url}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Step 5: Close the browser
        driver.quit()

    return results

