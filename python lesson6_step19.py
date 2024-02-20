# Для загрузки файла на веб - страницу, используем метод send_keys("путь к файлу")
# Три способа задать путь к файлу:
# 1. вбить руками
# element.send_keys("/home/user/stepik/Chapter2/file_example.txt")
# 2.задать с помощью переменных
# указывая директорию,где лежит файлу.txt, в конце должен быть /
# directory = "/home/user/stepik/Chapter2/"
# имя файла, который будем загружать на сайт
# file_name = "file_example.txt"
# собираем путь к файлу
# file_path = os.path.join(directory, file_name)
# отправляем файл
# element.send_keys(file_path)
# 3. путь автоматизатора.если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге

# импортируем модуль
# import os

# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
# current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
# file_name = "file_example.txt"

# получаем путь к file_example.txt
# file_path = os.path.join(current_dir, file_name)

# отправляем файл
# element.send_keys(file_path)


# итоговый код:

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ivan")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Ivan")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()