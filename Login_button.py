from selenium import webdriver
from selenium.webdriver.common.by import By

def verify_login_button(url):
    """
    Test whether the login button is visible and clickable.
    :param url: The URL of the webpage.
    :return: Dictionary with results for visibility and clickability.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    results = {"visible": False, "clickable": False}
    try:
        driver.get(url)

        # Locate the login button
        login_button = driver.find_element(By.XPATH, "//*[@id='login-btn']")  # Update XPath based on the actual element

        # Check if the button is visible
        if login_button.is_displayed():
            print("Test Passed: Login button is visible.")
            results["visible"] = True
        else:
            print("Test Failed: Login button is not visible.")

        # Check if the button is clickable
        try:
            login_button.click()
            print("Test Passed: Login button is clickable.")
            results["clickable"] = True
        except Exception as e:
            print(f"Test Failed: Login button is not clickable. Error: {e}")
    except Exception as e:
        print(f"Test Failed: An error occurred while locating the login button - {e}")
    finally:
        driver.quit()
    return results
