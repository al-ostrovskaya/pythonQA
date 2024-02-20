#Выбор из выпадающего списка
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(link)


browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()

#ВАриант 2 с подключением библиотеки Селекта

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))

select.select_by_value("1") # ищем по значению
select.select_by_visible_text("Python") # ищет элемент по видимому тексту,
select.select_by_index(1) #ищет по индексу, начиная с 0