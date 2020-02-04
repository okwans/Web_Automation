from selenium import webdriver
import time

browser = webdriver.Chrome(r'C:\chromedriver.exe')
browser.get("http://python.org")
time.sleep(5)

#menus = browser.find_elements_by_css_selector('#top ul.menu li')
#menus = browser.find_elements_by_css_selector('ol.flex-control-nav.flex-control-paging li')
#menus = browser.find_elements_by_css_selector('ul.navigation.menu')
"""
//*[@id="search"]
//*[@id="mainnav"]/ul
"""
menus = browser.find_elements_by_xpath('//*[@id="mainnav"]/ul')
#동작되는것


pypi = None
for m in menus:
    if m.text == "Documentation":
        pypi = m
    print(m.text)
    time.sleep(1)

pypi.click()  # 클릭

time.sleep(5)  # 5초 대기
browser.quit()  # 브라우저 종료