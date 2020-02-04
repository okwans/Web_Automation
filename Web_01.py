from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.get("http://www.youtube.com/")

time.sleep(5)

search = driver.find_element_by_xpath('//*[@id="search"]')

search.send_keys('Humax')
time.sleep(5)

search.send_keys(Keys.ENTER)
#btn = driver.find_element_by_id('search-icon-legacy')
#btn.click()
#time.sleep(5)
time.sleep(5)

continue_link = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[4]/div[1]/div/div[1]/div/h3/a')
continue_link.click()
time.sleep(30)

driver.quit()