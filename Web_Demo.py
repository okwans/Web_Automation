from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time, datetime
import cv2
import numpy as np
import unittest

class WebTestDemo(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome(r'C:\chromedriver.exe')
        #driver.get("https://gitlab.winant.co.kr:8443/")
        time.sleep(5)

    def test_WebDemo(self):
        driver = webdriver.Chrome(r'C:\chromedriver.exe')
        driver.get("https://gitlab.winant.co.kr:8443/")
        time.sleep(5)

        ID = driver.find_element_by_id('tl_login')
        PW = driver.find_element_by_id('tl_password')
        LoginBTN = driver.find_element_by_xpath('//input[@type="submit"]')
        time.sleep(2)

        ID.send_keys('ksoh')
        PW.send_keys('oks9678045@!')
        LoginBTN.send_keys(Keys.ENTER)
        time.sleep(5)
        """
        html = browser.execute_script('return document.body.innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        #notice = soup.select('div')
        for m in soup:
            print(m)
            #time.sleep(1)
        """

        iframes = driver.find_elements_by_css_selector('frame')
        for iframe in iframes:
            print(iframe.get_attribute('name'))

        time.sleep(5)

        driver.switch_to.frame('mainframe')

        driver.find_element_by_link_text('Requirement Specification').click()
        time.sleep(5)

        iframes = driver.find_elements_by_css_selector('frame')
        for iframe in iframes:
            print(iframe.get_attribute('name'))

        driver.switch_to.frame('treeframe')

        driver.find_element_by_id('expand_tree').click()
        time.sleep(5)

        """
        driver.switch_to.default_content()
        iframes = driver.find_elements_by_css_selector('frame')
        for iframe in iframes:
            print(iframe.get_attribute('name'))

        driver.switch_to.frame('mainframe')
        driver.switch_to.frame('treeframe')
        """

        driver.find_element_by_xpath('/html/body/div[2]/div/div/ul/li/ul/li[4]/ul/li[1]/ul/li[1]/div/a/span').click()
        time.sleep(5)

        driver.switch_to.default_content()
        driver.switch_to.frame('mainframe')
        driver.switch_to.frame('workframe')

        time.sleep(3)

        data = driver.find_elements_by_xpath('/html/body/div/table[1]/tbody/tr[6]/td/fieldset')
        time.sleep(3)

        for m in data:
            print(m.text)
            # time.sleep(1)
        time.sleep(3)

        # 화면 비교 - 1 ==> Pass 일때
        template_temp = cv2.imread("TestImage.jpg")
        template = cv2.cvtColor(template_temp, cv2.COLOR_BGR2GRAY)
        driver.save_screenshot('Original.png')
        Origin_Image_temp = cv2.imread("Original.png")
        Origin_Image = cv2.cvtColor(Origin_Image_temp, cv2.COLOR_BGR2GRAY)
        # method = eval('cv2.TM_CCOEFF')
        res = cv2.matchTemplate(Origin_Image, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(min_val)
        print(max_val)
        time.sleep(5)

        if max_val > 800000000:
            print("Test :: Pass!!!")
        else:
            print("Test :: Fail!!!")
        time.sleep(5)

        # 화면 비교 - 2 ==> Fail 일때
        template_temp = cv2.imread("Driver.png")
        template = cv2.cvtColor(template_temp, cv2.COLOR_BGR2GRAY)
        driver.save_screenshot('Original.png')
        Origin_Image_temp = cv2.imread("Original.png")
        Origin_Image = cv2.cvtColor(Origin_Image_temp, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(Origin_Image, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(min_val)
        print(max_val)
        time.sleep(5)

        if max_val > 800000000:
            print("Test :: Pass!!!")
        else:
            print("Test :: Fail!!!")
        time.sleep(5)

        driver.switch_to.default_content()
        driver.switch_to.frame('mainframe')
        driver.switch_to.frame('treeframe')

        driver.find_element_by_id('extdd-6').click()
        time.sleep(5)

        driver.switch_to.default_content()
        driver.switch_to.frame('mainframe')
        driver.switch_to.frame('workframe')

        images = driver.find_elements_by_css_selector('img.clickable')
        for image in images:
            print(image.get_attribute('src'))
            if image.get_attribute('src') == 'https://gitlab.winant.co.kr:8443/gui/themes/default/images/cog.png':
                image.click()

        time.sleep(3)

        btns = driver.find_elements_by_css_selector('input')
        for btn in btns:
            print(btn.get_attribute('name'))
            # time.sleep(1)
            if btn.get_attribute('name') == 'create_req':
                btn.click()
                break
        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div/form/div[4]/input').send_keys('Test_DocumentID')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/form/div[6]/input').send_keys('Title')
        time.sleep(2)

        """
        ckeditor_frame = driver.find_element(:class => 'cke_wysiwyg_frame')
        driver.switch_to.frame(ckeditor_frame)
        editor_body = driver.find_element(:tag_name => 'body')
        editor_body.send_keys("<h1>Heading</h1>Yi Zeng")
        """

        driver.execute_script(('CKEDITOR.instances.scope.setData("<h1>CarPlat</h1>Selenium Test")'))

        time.sleep(5)
        driver.quit()


    def tearDown(self):
        #self.driver.quit()
        time.sleep(5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WebTestDemo)
    unittest.TextTestRunner(verbosity=2).run(suite)