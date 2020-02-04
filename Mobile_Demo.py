import unittest
import os
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import base64

import cv2
import numpy as np
import time, datetime


class Matching():

    def detectimage(self, screenshotPath, detectImagePath):
        sourceimage = cv2.imread(screenshotPath, 0)
        source_demensions = sourceimage.shape

        template_temp = cv2.imread(detectImagePath, 0)
        template_demention = template_temp.shape

        threshold = source_demensions[1] / 720
        x = source_demensions[1] / 720
        y = source_demensions[0] / 1280
        print(threshold)
        template_resize = cv2.resize(template_temp, dsize=(int(template_demention[1] * threshold), int(template_demention[0] * threshold)), interpolation=cv2.INTER_AREA)
        cv2.imwrite(detectImagePath + '_resize.png', template_resize)

        template = cv2.imread(detectImagePath + '_resize.png', 0)

        w, h = template.shape[::-1]

        #method = eval('cv2.TM_CCOEFF')
        res = cv2.matchTemplate(sourceimage, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print('max_val: %d' % max_val)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = (top_left[0] + int(w/2), top_left[1] + int(h/2))
        print(center)
        #color = (0, 0, 255)
        #cv2.rectangle(sourceimage, top_left, bottom_right, color, thickness=8)

        #detectshotPath = screenshotPath[:-4] + '-detect.png'
        #cv2.imwrite(detectshotPath, sourceimage)

        return center, x, y

class MobileTestDemo(unittest.TestCase):

    def setUp(self):
        app = os.path.join(os.path.dirname(__file__), 'C:\\OpenCV_Log', 'carplat.apk')
        app = os.path.abspath(app)
        """
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4770/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "deviceName": "Android Emulator",
                "app": app,
                "automationName": "Appium",
                "newCommandTimeout": 300,
                "appPackage": "kr.co.plat.carplat.dev",
                "appActivity": "kr.co.plat.carplat.fragment.main.SplashActivity"
            })
        """
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "platformVersion": "7",
                "deviceName": "Glaxy",
                "app": app,
                "automationName": "Appium",
                "newCommandTimeout": 300,
                "appPackage": "kr.co.plat.carplat.dev",
                "appActivity": "kr.co.plat.carplat.fragment.main.SplashActivity",
                "udid": "02157df279e97104"
            })


    def makeTS(self):
        return str(int(datetime.datetime.now().timestamp()))

    def strDatetime(self):
        return str(datetime.datetime.now().strftime("%Y%m%d%H%M"))

    def test_01_LoginPass(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        time.sleep(5)

        # 동영상 Recording 동작하기
        driver.start_recording_screen()

        # Test 시나리오
        user_action = TouchAction(driver)
        time.sleep(5)

        # allow 선택
        allow = wait.until(
            EC.element_to_be_clickable((By.ID, "com.android.packageinstaller:id/permission_allow_button")))
        allow.click()
        # driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        print("위치 정보에 대해 allow 선택")
        time.sleep(5)

        # 로그인/회원가입
        login = wait.until(EC.element_to_be_clickable((By.ID, "kr.co.plat.carplat.dev:id/toolbar_title")))
        login.click()
        print("로그인/회원가입 탭")
        time.sleep(5)

        # 로그인 탭
        # user_action = TouchAction(driver)
        # user_action.tap(x=1287, y=207).perform()
        driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView').click()
        print("로그인 탭")
        time.sleep(5)

        # 사용자 ID 입력
        driver.find_element_by_id("kr.co.plat.carplat.dev:id/let_text").send_keys("okwans@naver.com")
        # eli1= wait.until(EC.element_to_be_clickable((By.ID, "kr.co.plat.carplat.dev:id/let_text")))
        # eli1.send_keys("okwans@naver.com")
        print("ID 입력")
        time.sleep(3)

        # 사용자 PW 입력
        # eli2 = driver.find_element_by_id("kr.co.plat.carplat.dev:id/fragment_login_password")
        eli2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText")
        eli2.send_keys("oks9678045")
        print("PW 입력")
        time.sleep(3)

        # 로그인 버튼 누름
        driver.find_element_by_id("kr.co.plat.carplat.dev:id/fragment_login_btn_email").click()
        print("Login 완료")
        time.sleep(5)

        # 운전면허 나중에 등록하기
        matching = Matching()

        #test_folder_name = self.strDatetime()
        currentPath = '%s/' % os.getcwd()
        #test_Directory = currentPath + test_folder_name + '/'
        #test_Directory = 'C:/Users/ksoh/PycharmProjects/Source/Web_AutoTest/'

        #if not os.path.exists(test_Directory):
        #    os.makedirs(test_Directory)
        #time.sleep(5)

        screenshotPath = currentPath + 'screenshot.png'
        detectImagePath = currentPath + 'Driver.png'
        driver.save_screenshot(screenshotPath)
        print("화면 캡쳐")
        time.sleep(5)

        center, x_threshold, y_threshold = matching.detectimage(screenshotPath, detectImagePath)
        driver.tap([center])
        print("이미지 비교하여 운전면허 나중에 등록하기 탭 동작 수행")
        print("x,y threshold 값")
        print(x_threshold, y_threshold)
        time.sleep(5)

        # 지도에서 "여기서 받기" 탭
        driver.find_element_by_id('kr.co.plat.carplat.dev:id/fragment_filter_map_marker').click()
        print("지도에서 여기서받기 선택")
        time.sleep(5)

        # 수령장소와 반납 장소는 default로 정의 후, 반납장소 선택완료 버튼 탭
        driver.find_element_by_id('kr.co.plat.carplat.dev:id/fragment_map_pick_done_button').click()
        print("반납장소 선택완료 버튼 탭")
        time.sleep(5)

        # 시작일은 default 날짜로 사용
        # 설정완료 버튼 캡
        driver.find_element_by_id('kr.co.plat.carplat.dev:id/datetime_picker_confirm').click()
        print("시작일 설정완료 버튼 탭")
        time.sleep(5)

        # Picker에서 임의의 미래 일자로 이동
        for coount in range(0,20):
            TouchAction(driver).press(x=int(177*x_threshold), y=int(733*y_threshold)).move_to(x=int(179*x_threshold), y=int(583*y_threshold)).release().perform()
            temp = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.NumberPicker/android.widget.EditText')
            if temp.text == '01월 18일 토':
                print("'완료일을 01월 18일 토'로 확인 후, 설정")
                break
            time.sleep(3)

        # 설정완료 버튼 캡
        driver.find_element_by_id('kr.co.plat.carplat.dev:id/datetime_picker_confirm').click()
        print("설정완료 버튼 탭")
        time.sleep(5)

        # 차량 선택 항목에서 중형 선택
        temp = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]')
        temp.click()
        time.sleep(5)

        # 차종 선택 완료
        driver.find_element_by_id('kr.co.plat.carplat.dev:id/fragment_filter_size_search').click()
        print("차종 선택완료 버튼 탭")
        time.sleep(5)

        # 차량 선택 완료
        driver.find_element_by_id('kr.co.plat.carplat.dev:id/minPrice').click()
        print("차량 선택완료 탭")
        time.sleep(5)

        # 차량 선택 완료
        driver.find_element_by_id('kr.co.plat.carplat.dev:id/price').click()
        print("최종 선택 완료")
        time.sleep(5)

        print("우선 여기까지 Demo 진행 완료!!!")
        time.sleep(5)

        # 동영상 Stop후, Recording 파일 만들고 저장하기
        video_rawdata = driver.stop_recording_screen()
        video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")
        filepath = os.path.join(currentPath, video_name + ".mp4")
        with open(filepath, "wb") as vd:
            vd.write(base64.b64decode(video_rawdata))

    #def test_02_LoginFail(self):


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MobileTestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)