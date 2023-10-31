import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service():
    global driver
    try:
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:5000")

        # Find the element by XPath
        element = driver.find_element(By.XPATH, "/html/body/ul/li")

        # Get the text from the element
        element_text = element.text

        # Split the text to extract the number
        parts = element_text.split(':')
        if len(parts) == 2:
            score = parts[1].strip()
            print(f"Score: {score}")

            # Convert the score to an integer for testing
            score = int(score)

            if 1 <= score <= 1000:
                print("Pass")
                return True
            else:
                print("Fail")
                return False

    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    test_scores_service()
