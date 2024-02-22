from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

class TestClass():

    def test_class_name(self):
        link = "https://stepik.org/lesson/236895/step/1"
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        browser = webdriver.Chrome(options=options)
        browser.get(link)
        browser.implicitly_wait(5)
        self.input0 = browser.find_element(By.CSS_SELECTOR, "#ember33").click()
        self.input1 = browser.find_element(By.NAME, "login")
        self.input1.send_keys("login")
        self.input2 = browser.find_element(By.NAME, "password")
        self.input2.send_keys("password")
        self.input3 = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        browser.implicitly_wait(5)
        y = math.log(int(time.time()))
        answer = browser.find_element(By.CSS_SELECTOR, ".quiz-component textarea")
        answer.send_keys(y)
        self.input4 = browser.find_element(By.CSS_SELECTOR, ".submit-submission").click
