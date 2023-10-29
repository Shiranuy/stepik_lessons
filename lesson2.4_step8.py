import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    check = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )




    input4 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    input4.click()
    
    time.sleep(1)
    
    

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    
   
    
    
  
    
    input4 = browser.find_element(By.ID, 'solve')
    input4.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
    

# не забываем оставить пустую строку в конце файла