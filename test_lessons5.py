from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_find_element = browser.find_element(By.ID, "input_value")
    x = x_find_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 110);")

    input1 = browser.find_element(By.ID, "answer").send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']").click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']").click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()



finally:
    time.sleep(20)
    browser.quit()