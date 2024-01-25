import requests
import os
from bs4 import BeautifulSoup
import os

'''
URL에 있는 이미지 다운로드 하기
2023-06-26
'''
def download_url_image(url):
        
    url = "https://example.com" # 웹 페이지 URL

    # 웹 페이지의 HTML을 가져옵니다.
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # HTML에서 img 태그를 모두 찾습니다.
    img_tags = soup.find_all('img')

    # 각 img 태그에서 src 속성 (이미지 URL)을 추출하고 이미지를 다운로드합니다.
    for img in img_tags:
        img_url = img['src']
        img_name = os.path.basename(img_url)
        
        # 이미지 URL로부터 이미지 데이터를 가져옵니다.
        img_response = requests.get(img_url, stream=True)

        # 이미지를 파일로 저장합니다.
        with open(img_name, 'wb') as f:
            for chunk in img_response.iter_content(1024):
                f.write(chunk)
