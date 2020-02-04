from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# TouchAction을 하기위한 Lib를 Import
import time
from time import sleep
import os
import base64


desired_cap = {
  "platformName": "Android",
  "platformVersion": "7",
  "deviceName": "Glaxy",
  "app": "C:\\OpenCV_Log\\carplat.apk",
  "automationName": "Appium",
  "newCommandTimeout": 300,
  "appPackage": "kr.co.plat.carplat.dev",
  "appActivity": "kr.co.plat.carplat.fragment.main.SplashActivity",
  "udid": "02157df279e97104"
}
"""
desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": "C:\\OpenCV_Log\\carplat.apk",
  "automationName": "Appium",
  "newCommandTimeout": 300,
  "appPackage": "kr.co.plat.carplat.dev",
  "appActivity": "kr.co.plat.carplat.fragment.main.SplashActivity"
}
"""

# App 실행
driver = webdriver.Remote("http://localhost:4722/wd/hub", desired_cap)
driver.implicitly_wait(30)
time.sleep(5)

# 동영상 Recording 동작하기
#driver.start_recording_screen()

user_action = TouchAction(driver)
wait = WebDriverWait(driver, 20)

time.sleep(5)
#allow 선택
allow = wait.until(EC.element_to_be_clickable((By.ID, "com.android.packageinstaller:id/permission_allow_button")))
allow.click()
#driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
time.sleep(5)

#로그인/회원가입
login = wait.until(EC.element_to_be_clickable((By.ID, "kr.co.plat.carplat.dev:id/toolbar_title")))
login.click()
time.sleep(5)

#로그인 탭
#user_action = TouchAction(driver)
#user_action.tap(x=1287, y=207).perform()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView').click()
time.sleep(5)

#사용자 ID 입력
driver.find_element_by_id("kr.co.plat.carplat.dev:id/let_text").send_keys("okwans@naver.com")
#eli1= wait.until(EC.element_to_be_clickable((By.ID, "kr.co.plat.carplat.dev:id/let_text")))
#eli1.send_keys("okwans@naver.com")
time.sleep(3)

#사용자 PW 입력
#eli2 = driver.find_element_by_id("kr.co.plat.carplat.dev:id/fragment_login_password")
eli2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText")
eli2.send_keys("oks9678045")
time.sleep(3)

#로그인 버튼 누름
driver.find_element_by_id("kr.co.plat.carplat.dev:id/fragment_login_btn_email").click()
time.sleep(5)

driver.quit()
# 동영상 Stop후, Recording 파일 만들고 저장하기
#video_rawdata = driver.stop_recording_screen()
#video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")
#filepath = os.path.join("C:\\Users\\ksoh\\PycharmProjects\\Source\\Appium\\", video_name+".mp4")

#with open(filepath,"wb") as vd:
#  vd.write(base64.b64decode(video_rawdata))