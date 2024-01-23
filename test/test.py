# -*- coding: utf-8 -*-
# Python 파일의 인코딩을 UTF-8로 지정합니다.

from webdriver_manager.chrome import ChromeDriverManager
# ChromeDriverManager를 임포트하여 크롬 드라이버를 자동으로 관리합니다.

from selenium import webdriver
# Selenium 웹드라이버를 임포트합니다.

from selenium.webdriver.chrome.service import Service
# Chrome 서비스 관련 기능을 임포트합니다.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 요소가 나타날 때까지 기다리는 기능을 임포트합니다.

from selenium.webdriver.common.by import By
# 요소를 찾을 때 사용하는 By 객체를 임포트합니다.

from selenium.webdriver.common.keys import Keys
# 키보드 키 상수를 임포트합니다 (예: Keys.ENTER).

import onetimepass as otp
# OTP(일회용 비밀번호) 생성 라이브러리를 임포트합니다.

import time, logging
# time 모듈과 logging 모듈을 임포트합니다.

from selenium.common.exceptions import WebDriverException
# Selenium의 WebDriverException 예외를 임포트합니다.

# 로깅 설정
logging.basicConfig(filename='error_log.log', level=logging.ERROR)
# 로깅을 설정하여 에러 메시지를 'error_log.log' 파일에 기록합니다.

def selenium_Login_google(userId, userPassword, userQrCode=None):
    # Google 로그인을 위한 함수를 정의합니다. userQrCode는 옵셔널 파라미터입니다.

    try:
        url = "https://accounts.google.com/"
        # Google 로그인 URL을 지정합니다.

        options = webdriver.ChromeOptions()
        # Chrome 옵션 객체를 생성합니다.

        # 여러 Chrome 옵션을 설정합니다.
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("detach", True)

        service = Service(executable_path=ChromeDriverManager().install())
        # ChromeDriverManager를 통해 Chrome 드라이버를 설치하고 서비스 객체를 생성합니다.

        driver = webdriver.Chrome(options=options, service=service)
        # WebDriver 객체를 생성합니다.

        driver.get(url)
        # 지정된 URL로 이동합니다.

        # ID 입력
        id_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "identifierId")))
        id_input.send_keys(userId + Keys.ENTER)
        # 사용자 ID를 입력하고 엔터를 누릅니다.

        time.sleep(5)

        # PASSWORD 입력
        pw_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "Passwd")))
        pw_input.send_keys(userPassword + Keys.ENTER)
        # 사용자 비밀번호를 입력하고 엔터를 누릅니다.

        time.sleep(5)

        # OTP 입력
        if userQrCode:
            otp_num = otp.get_totp(userQrCode)
            if len(str(otp_num)) == 5:
                otp_num = "0" + str(otp_num)
            otp_input = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="totpPin"]')))
            otp_input.send_keys(otp_num, Keys.ENTER)
            # OTP를 생성하고 입력합니다.

    except WebDriverException as e:
        # WebDriver 관련 예외를 처리합니다.
        print(f"WebDriver 오류 발생: {e}")
        logging.error(f"WebDriver 오류: {e}")

    except Exception as e:
        # 그 외 일반 예외를 처리합니다.
        print(f"예외 발생: {e}")
        logging.error(f"일반 오류: {e}")
        print()

    # finally:
    #     driver.quit()
    # WebDriver를 종