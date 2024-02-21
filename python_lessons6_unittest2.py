from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class class_name(unittest.TestCase):


    def test_class_name(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        self.input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required='']")
        self.input1.send_keys("Test")
        self.input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required='']")
        self.input2.send_keys("Test")
        self.input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required='']")
        self.input3.send_keys("Test")
        time.sleep(5)

        # Отправляем заполненную форму
        self.button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        self.button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        self.welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        self.assertEqual("Congratulations! You have successfully registered!" , self.welcome_text, msg=None)

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_class_name_dva(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        self.input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required='']")
        self.input1.send_keys("Test")
        self.input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required='']")
        self.input2.send_keys("Test")
        self.input3 = browser.find_element(By.XPATH, "//input[@class='form-control third' and @required='']")
        self.input3.send_keys("Test")


        # Отправляем заполненную форму
        self.button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        self.button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        self.welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        self.welcome_text = self.welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" , self.welcome_text, msg=None)


        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()