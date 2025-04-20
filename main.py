from Login_page import verify_url_using_find_element
from Webpage_Title import verify_webpage_title
from Login_button import verify_login_button
from Sign_up_button import verify_signup_button
from Sign_In import verify_signup_navigation
from Login_Logout import guvi_login_logout
from Invalid_Login import guvi_invalid_login


if __name__ == "__main__":
    test_url = "https://www.guvi.in"
    test_url_login = "https://www.guvi.in/sign-in/"
    expected_title = "GUVI | Learn to code in your native language"
    expected_signin_url = "https://www.guvi.in/register/"
    expected_url = "https://www.guvi.in/courses/?current_tab=myCourses"
    user_email = "gdekate103@gmail.com"
    user_password = "Gani@103@G"
    guvi_login_url = "https://www.guvi.in/login"
    invalid_email = "gdekate@example.com"
    invalid_password = "Gani@103@D"
    error_message_xpath = "//*[@id='emailgroup']/div"


    # Test Case 1: Verify URL Validity
    is_url_valid = verify_url_using_find_element(test_url)
    print(f"URL Validation Result: {is_url_valid}")

    # Test Case 2: Verify Webpage Title
    is_title_correct = verify_webpage_title(test_url, expected_title)
    print(f"Title Validation Result: {is_title_correct}")

    # Test Case 3: Verify Login Button Visibility and Clickability
    login_button_results = verify_login_button(test_url)
    print(f"Login Button Validation Results: {login_button_results}")

    # Test Case 4: Verify Sign-Up Button
    signup_button_results = verify_signup_button(test_url)
    print(f"Sign-Up Button Validation Results: {signup_button_results}")

    # Test Case 5: Verify signup_navigation
    print("Verify Navigation to Sign-In Page")
    verify_signup_navigation(test_url_login, expected_signin_url)

    # Test Case 6: Verify login logout
    results = guvi_login_logout(guvi_login_url, user_email, user_password,test_url,expected_url)
    print(f"Login and Logout Results: {results}")

    # Test Case 7: Verify invalid login
    error_message = guvi_invalid_login(guvi_login_url, invalid_email, invalid_password,error_message_xpath)
    if error_message:
        print(f"Captured Error Message: {error_message}")
    else:
        print("No error message was found.")
