import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test..")
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

# @pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
@pytest.mark.parametrize('lesson', ["236896", "236898", "236899"])
class TestMainPage2():
    def test_login_stepik(self, browser,lesson):
        link = f"https://stepik.org/lesson/{lesson}/step/1/"
        browser.implicitly_wait(10)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#ember33").click()
        self.input1 = browser.find_element(By.CSS_SELECTOR, "[type='email']")
        self.input1.send_keys("email")
        self.input2 = browser.find_element(By.CSS_SELECTOR, "[type='password']")
        self.input2.send_keys("password")
        self.input3 = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(5)
        self.check = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        self.check_answer = self.check.text


        if self.check_answer == None:
            browser.implicitly_wait(10)
            self.new_solve = browser.find_element(By.CSS_SELECTOR, ".again-btn").click()
            time.sleep(5)
            self.x = math.log(int(time.time()))
            self.answer = browser.find_element(By.CSS_SELECTOR, ".quiz-component textarea")
            self.answer.send_keys(self.x)
            browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
            self.y_element = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
            self.y = self.y_element.text
            assert self.y == "Correct!", "Answer need be Correct!"
            browser.close()
        else:
            self.x = math.log(int(time.time()))
            self.answer = browser.find_element(By.CSS_SELECTOR, ".quiz-component textarea")
            self.answer.send_keys(self.x)
            browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
            self.y_element = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
            self.y = self.y_element.text
            assert self.y == "Correct!", "Answer need be Correct!"
            browser.close()






