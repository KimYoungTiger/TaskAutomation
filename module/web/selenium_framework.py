# -*- coding: utf-8 -*-
import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException

# 로깅 설정
logging.basicConfig(filename='error_log.log', level=logging.ERROR)


def selenium_framework(): 

    try:
        url = "http://www.taskautomation.tistory.com"
        options = webdriver.ChromeOptions()
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(url)

        # 셀레늄 개발 코드
        # ...
        
    # WebDriver에서 발생한 예외 처리
    except WebDriverException as e:
        print(f"WebDriver 오류 발생: {e}")
        logging.error(f"WebDriver 오류: {e}")

    # 기타 모든 예외 처리
    except Exception as e:
        print(f"예외 발생: {e}")
        logging.error(f"일반 오류: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    selenium_framework()
