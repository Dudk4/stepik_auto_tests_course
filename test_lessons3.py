from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum(x, y):
    return str(int(x) + int(y))


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_find_element = browser.find_element(By.ID, "num1")
    x = x_find_element.text
    y_find_element = browser.find_element(By.ID, "num2")
    y = y_find_element.text

    a = sum(x, y)
    print(a)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(a))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()




finally:
    time.sleep(10)
    browser.quit()

