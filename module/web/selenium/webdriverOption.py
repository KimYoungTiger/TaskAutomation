from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--window-size')
options.add_argument('--start-maximized')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--disable-infobars')
options.add_argument('--incognito')
options.add_argument('--disable-popup-blocking')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-setuid-sandbox')
options.add_argument('--user-data-dir')
options.add_argument('--remote-debugging-port')
options.add_argument('--lang')
options.add_argument('--proxy-server')
options.add_argument('--proxy-bypass-list')
options.add_argument('--auto-open-devtools-for-tabs')
options.add_argument('--disable-web-security')



'''
options.add_argument("--headless")  # GUI 없이 백그라운드에서 브라우저 실행
options.add_argument("--no-sandbox")  # 샌드박스 모드 비활성화
options.add_argument("--disable-gpu")  # GPU 하드웨어 가속 비활성화
options.add_argument("--window-size=1920x1080")  # 창 크기 지정
options.add_argument("--start-maximized")  # 창 최대화
options.add_argument("--disable-dev-shm-usage")  # /dev/shm 사용 비활성화
options.add_argument("--disable-extensions")  # 확장 기능 비활성화
options.add_argument("--disable-infobars")  # 정보 표시줄 비활성화
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")  # 사용자 에이전트 설정
options.add_argument("--allow-insecure-localhost")  # 불안전한 localhost 허용
options.add_argument("--ignore-certificate-errors")  # SSL 인증서 오류 무시
options.add_argument("--allow-running-insecure-content")  # 불안전한 컨텐츠 실행 허용

--headless: 브라우저를 GUI 없이 백그라운드에서 실행합니다.
--no-sandbox: 샌드박스 모드를 비활성화합니다. 주로 Docker와 같은 컨테이너 환경에서 사용됩니다.
--disable-gpu: GPU 하드웨어 가속을 비활성화합니다. 이전에는 특히 Linux에서 Headless 모드를 사용할 때 필요했습니다.
--window-size: 브라우저 창의 크기를 지정합니다. 예: --window-size=1920,1080.
--start-maximized: 브라우저를 최대화된 상태로 시작합니다.
--disable-dev-shm-usage: /dev/shm 사용을 비활성화합니다. Docker에서 유용할 수 있습니다.
--disable-extensions: 모든 Chrome 확장 기능을 비활성화합니다.
--disable-infobars: Chrome이 자동화된 소프트웨어에 의해 제어된다는 정보 표시줄을 비활성화합니다.
--incognito: 익명(시크릿) 모드로 브라우저를 시작합니다.
--disable-popup-blocking: 팝업 차단 기능을 비활성화합니다.
--allow-insecure-localhost: HTTPS 오류를 무시하고 개발 중인 로컬 호스트에서의 불안전한 연결을 허용합니다.
--ignore-certificate-errors: SSL 인증서 오류를 무시합니다.
--disable-setuid-sandbox: 브라우저 프로세스의 권한 상승을 방지하는 샌드박스 기능을 비활성화합니다.
--user-data-dir: 사용자 데이터(북마크, 히스토리 등)와 캐시를 저장할 디렉터리를 지정합니다.
--remote-debugging-port: 원격 디버깅을 위한 포트를 지정합니다.
--lang: 브라우저의 언어를 설정합니다. 예: --lang=en-US.
--proxy-server: 브라우저의 프록시 서버를 지정합니다.
--proxy-bypass-list: 프록시를 거치지 않을 호스트나 도메인을 지정합니다.
--auto-open-devtools-for-tabs: 브라우저를 열 때 개발자 도구를 자동으로 엽니다.
--disable-web-security: 웹 보안 기능을 비활성화합니다. 주의해서 사용해야 합니다.
'''