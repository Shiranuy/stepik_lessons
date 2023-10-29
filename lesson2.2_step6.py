import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    
    
    browser.execute_script("window.scrollBy(0, 200);")
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()
    
    input4 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    input4.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
    

# не забываем оставить пустую строку в конце файла