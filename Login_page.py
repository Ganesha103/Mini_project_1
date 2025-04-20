from selenium import webdriver
from selenium.webdriver.common.by import By

def verify_url_using_find_element(url):
    """
    Function to test whether a given URL is valid and accessible using find_element.
    :param url: URL to be tested
    """
    # Set up WebDriver (provide the path to your ChromeDriver)
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        # Navigate to the URL
        driver.get(url)

        # Attempt to locate a key element using find_element
        element = driver.find_element(By.TAG_NAME, "body")  # You can change this to a specific element on GUVI

        # If the element is found, the URL is valid
        if element:
            print("Test Passed: The URL is valid and accessible.")
            return True
    except Exception as e:
        # If an error occurs, the URL might not be accessible
        print(f"Test Failed: An error occurred - {e}")
        return False
    finally:
        # Close the browser
        driver.quit()
