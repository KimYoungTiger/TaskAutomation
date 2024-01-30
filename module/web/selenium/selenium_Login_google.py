# -*- coding: utf-8 -*-
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import onetimepass as otp
import time, logging
from selenium.common.exceptions import WebDriverException

# 로깅 설정
logging.basicConfig(filename='error_log.log', level=logging.ERROR)


def selenium_Login_google(userId, userPassword, userQrCode=None):

    try:
        url = "https://accounts.google.com/"
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("detach", True)
        
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)

        driver.get(url)

        # ID
        id_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "identifierId")))
        id_input.send_keys(userId + Keys.ENTER)
        time.sleep(5)

        # PASSWORD
        pw_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "Passwd")))
        pw_input.send_keys(userPassword + Keys.ENTER)
        time.sleep(5)

        # OTP 입력시
        if userQrCode:
            otp_num = otp.get_totp(userQrCode)
            if len(str(otp_num)) == 5:
                otp_num = "0" + str(otp_num)
            otp_input = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="totpPin"]')))
            otp_input.send_keys(otp_num, Keys.ENTER)

    except WebDriverException as e:
        # WebDriver에서 발생한 예외 처리
        print(f"WebDriver 오류 발생: {e}")
        logging.error(f"WebDriver 오류: {e}")

    except Exception as e:
        # 기타 모든 예외 처리
        print(f"예외 발생: {e}")
        logging.error(f"일반 오류: {e}")
        print()

    # finally:
    #     driver.quit()


if __name__ == "__main__":

    google_id = ""
    google_pw = ""

    selenium_Login_google(google_id, google_pw)
