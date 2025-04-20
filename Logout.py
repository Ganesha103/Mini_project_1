from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def guvi_login_logout(login_url, email, password, logout_button_xpath, expected_logout_url):

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

        # Verify successful login by checking redirected URL or user-specific element
        current_url = driver.current_url
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

        logout_button = driver.find_element(By.XPATH,logout_button_xpath)  # Replace with actual XPath for logout button
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


# Example usage
if __name__ == "__main__":
    guvi_login_url = "https://www.guvi.in/login"  # Replace with GUVI login page URL
    user_email = "gdekate103@gmail.com"        # Replace with your valid email
    user_password = "Gani@103@G"             # Replace with your valid password
    logout_button_xpath = "//div[text()='Sign Out']" # Replace with actual logout button XPath
    expected_logout_url = "https://www.guvi.in/"  # Replace with URL expected after logout
    expected_url = "https://www.guvi.in/courses/?current_tab=myCourses"

    results = guvi_login_logout(guvi_login_url, user_email, user_password, logout_button_xpath, expected_logout_url)
    print(f"Login and Logout Results: {results}")
