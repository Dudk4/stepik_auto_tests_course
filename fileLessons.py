from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname").send_keys("Я")
    input2 = browser.find_element(By.NAME, "lastname").send_keys("Победитель")
    input3 = browser.find_element(By.NAME, "email").send_keys("Мира")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    element = browser.find_element(By.CSS_SELECTOR, "[type = 'file']")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(20)
    browser.quit()

