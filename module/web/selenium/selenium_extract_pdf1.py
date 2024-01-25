# -*- coding: utf-8 -*-
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base64 import b64decode
import onetimepass as otp
import time

def notion_collect_bill():
    
    userId = ""
    userPassword = ""
    userQrCode = ""
    
    try:
        url = "https://www.notion.so/"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=ko_KR')
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
        
        driver.get(url)
        current_window = driver.current_window_handle

        # 구글 로그인 클릭
        google_login_object = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "googleLogo")))
        google_login_object.click()
        time.sleep(3)
    
        # 로그인 팝업 창으로 전환
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])
        
        # ID
        id_input =  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "identifierId")))
        id_input.send_keys(userId + Keys.ENTER)

        # PASSWORD
        pw_input =  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.NAME, "Passwd")))
        pw_input.send_keys(userPassword + Keys.ENTER)

        # OTP
        otp_num = otp.get_totp(userQrCode)
        if len(str(otp_num)) == 5 :
            otp_num = "0" + str(otp_num)
        otp_input = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="totpPin"]')))
        otp_input.send_keys(otp_num, Keys.ENTER)
        
        # 작업 완료 후, 원래 창으로 돌아가기
        time.sleep(5)
        driver.switch_to.window(current_window)

        # 사이드바에 설정 버튼 클릭 
        setting_btn = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME,"sidebarSettings")))
        setting_btn.click()

        # 설정 사이드에 청구 클릭 
        setting_btn = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME,"settingsBilling")))
        setting_btn.click()
        driver.implicitly_wait(10)

        # base window 저장
        current_window = driver.current_window_handle

        # 모든 청구서 find
        time.sleep(5) # 앞뒤의 시간 Delay 필수
        all_bills = driver.find_elements(By.XPATH, '//div[text()="청구서"]//following-sibling::*')
        time.sleep(5) # 앞뒤의 시간 Delay 필수

        for bill in all_bills:

            # "청구서 보기" 버튼 클릭
            button = WebDriverWait(bill, 10).until(EC.element_to_be_clickable((By.XPATH, './/div[@role="button"]')))
            button.click()
            driver.implicitly_wait(10)

            # 청구서 팝업 창으로 전환
            window_handles = driver.window_handles
            driver.switch_to.window(window_handles[-1])
            time.sleep(5)

            # PDF 파일로 저장
            a = driver.execute_cdp_cmd(
                "Page.printToPDF", {"path": 'html-page.pdf', "format": 'A4'})
            print(a)
            b64 = a['data']
            bytes = b64decode(b64, validate=True)

            # Error 확인
            if bytes[0:4] != b'%PDF':
                raise ValueError('Missing the PDF file signature')

            f = open(driver.title + '.pdf', 'wb')
            f.write(bytes)
            f.close()

            # 원래 창으로 돌아가기
            driver.close()
            driver.switch_to.window(current_window)
            driver.implicitly_wait(10)
    
    finally :
        driver.quit()

