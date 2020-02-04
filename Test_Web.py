from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\chromedriver.exe')

driver.implicitly_wait(3)

driver.get('https://www.naver.com')

elm = driver.find_elements(By.ID, 'query')[0]
elm.send_keys('개봉영화')

btn_elm = driver.find_elements(By.ID, 'search_btn')[0]
btn_elm.click()

driver.execute_script(
    "(function() { " +
    "window.open('https://www.naver.com', 'second');" +
    "})();"
)

driver.switch_to.window("second")
elm = driver.find_elements(By.ID, 'query')[0]
elm.send_keys('개봉예정영화')

btn_elm = driver.find_elements(By.ID, 'search_btn')[0]
btn_elm.click()

sleep(10)

driver.quit()
