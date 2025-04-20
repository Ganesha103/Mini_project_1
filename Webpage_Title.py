from selenium import webdriver

def verify_webpage_title(url, expected_title):
    """
    Function to test whether the webpage title matches the expected title.
    :param url: The URL of the webpage.
    :param expected_title: The expected title of the webpage.
    :return: True if the title matches, False otherwise.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        driver.get(url)
        actual_title = driver.title
        print(f"Actual Title: {actual_title}")
        if actual_title == expected_title:
            print("Test Passed: The title matches the expected title.")
            return True
        else:
            print("Test Failed: The title does not match the expected title.")
            return False
    except Exception as e:
        print(f"Test Failed: An error occurred - {e}")
        return False
    finally:
        driver.quit()
