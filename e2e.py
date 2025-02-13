from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time

def test_scores_service(app_url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.get(app_url)

        time.sleep(2)
        
        score_element = driver.find_element(By.ID, "score")
        score_text = score_element.text.strip()

        try:
            score = int(score_text)
        except ValueError:
            print(f"Invalid score format: {score_text}")
            driver.quit()
            return False

        if 1 <= score <= 1000:
            driver.quit()
            return True
        else:
            print(f"Score {score} is not between 1 and 1000.")
            driver.quit()
            return False

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main_function():
    app_url = "http://127.0.0.1:8777" 
    if test_scores_service(app_url):
        print("Test passed: Score is valid.")
        return 0
    else:
        print("Test failed: Invalid score.")
        return -1

if __name__ == "__main__":
    sys.exit(main_function())
