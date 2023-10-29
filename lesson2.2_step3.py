import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "https://suninjuly.github.io/selects1.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    time.sleep(5)
    take1 = browser.find_element(By.ID, 'num1').text
    take1 = int(take1)
    take2 = browser.find_element(By.ID, 'num2').text
    take2 = int(take2)
    take3 = take1 + take2
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(take3)) # ищем элемент с текстом "Python"
    time.sleep(1)
    input4 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    input4.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    browser.close()
    browser.quit()
    
    

# не забываем оставить пустую строку в конце файла