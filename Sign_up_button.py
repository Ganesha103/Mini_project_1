from selenium import webdriver
from selenium.webdriver.common.by import By

def verify_signup_button(url):
    """
    Test whether the Sign-Up button is visible, clickable, and enabled.
    :param url: The URL of the webpage.
    :return: Dictionary with results for visibility, clickability, and enabled state.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    results = {"visible": False, "clickable": False, "enabled": False}
    try:
        # Open the URL
        driver.get(url)

        # Locate the Sign-Up button (Update XPath based on the webpage structure)
        signup_button = driver.find_element(By.XPATH, "//a[text()='Sign up']")  # Replace with actual locator

        driver.implicitly_wait(10)
        # Check if the button is visible
        if signup_button.is_displayed():
            print("Test Passed: Sign-Up button is visible.")
            results["visible"] = True
        else:
            print("Test Failed: Sign-Up button is not visible.")

        # Check if the button is enabled
        if signup_button.is_enabled():
            print("Test Passed: Sign-Up button is enabled.")
            results["enabled"] = True
        else:
            print("Test Failed: Sign-Up button is disabled.")

        # Attempt to click the button if it is enabled
        if results["enabled"]:
            try:
                signup_button.click()
                print("Test Passed: Sign-Up button is clickable.")
                results["clickable"] = True
            except Exception as e:
                print(f"Test Failed: Sign-Up button is not clickable. Error: {e}")
    except Exception as e:
        print(f"Test Failed: An error occurred while locating the Sign-Up button - {e}")
    finally:
        driver.quit()
    return results

