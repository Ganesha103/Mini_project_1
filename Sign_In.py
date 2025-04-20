from selenium import webdriver
from selenium.webdriver.common.by import By

def verify_signup_navigation(url, expected_url):
    """
    Test whether the Sign-Up button redirects to the expected URL.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        driver.get(url)
        signup_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Signup')]")

        # Click the Sign-Up button
        signup_button.click()

        # Verify if the page navigates to the expected URL
        current_url = driver.current_url
        if current_url == expected_url:
            print("Test Passed: Navigation to sign-in page is successful.")
            return True
        else:
            print("Test Failed: Navigation to sign-in page is unsuccessful.")
            return False
    except Exception as e:
        print(f"Test Failed: An error occurred - {e}")
        return False
    finally:
        driver.quit()
