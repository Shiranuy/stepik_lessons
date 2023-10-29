import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    
    takevalue = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    y = calc(takevalue)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    time.sleep(1)
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()
    time.sleep(1)
    input4 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    input4.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    webdriver.close()
    time.sleep(2)
    driver.quit()

# не забываем оставить пустую строку в конце файла