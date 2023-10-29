import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os
link = "http://suninjuly.github.io/file_input.html"



 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

try:
    browser = webdriver.Chrome()
    browser.get(link)

    

    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
    input1.send_keys('Абс')
    
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
    input2.send_keys('зхс')
    
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
    input3.send_keys('pofigy@mail.ru')
    
    input4 = browser.find_element(By.CSS_SELECTOR, '[type=file]')
    input4.send_keys(file_path)
    
    input5 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    input5.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
    

# не забываем оставить пустую строку в конце файла