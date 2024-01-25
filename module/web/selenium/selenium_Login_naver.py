# -*- coding: utf-8 -*-
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, logging
from selenium.common.exceptions import WebDriverException

# 로깅 설정
logging.basicConfig(filename='error_log.log', level=logging.ERROR)


def selenium_Login_naver(userId, userPassword, userQrCode=None): 

    try:
        url = "https://www.naver.com/"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=ko_KR')
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)

        driver.get()

        # 코드 입력

    except WebDriverException as e:
        # WebDriver에서 발생한 예외 처리
        print(f"WebDriver 오류 발생: {e}")
        logging.error(f"WebDriver 오류: {e}")

    except Exception as e:
        # 기타 모든 예외 처리
        print(f"예외 발생: {e}")
        logging.error(f"일반 오류: {e}")
        print()

    finally:
        driver.quit()


if __name__ == "__main__":
    selenium_Login_naver()

