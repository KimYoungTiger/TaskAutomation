import cv2
import numpy as np
import pygetwindow as gw
import pyautogui

def record_window(window_title, output_filename='recording.avi', fps=10):
    # 특정 윈도우 찾기
    window = gw.getWindowsWithTitle(window_title)[0]
    window.moveTo(0,0)  # 윈도우를 화면 좌상단으로 이동 (선택적)
    window.activate()  # 윈도우 활성화

    # 녹화 설정
    codec = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
    out = cv2.VideoWriter(output_filename, codec, fps, (window.width, window.height))

    while True:  # 무한 루프로 녹화 시작
        # 윈도우의 스크린샷을 이미지로 캡처
        screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
        frame = np.array(screenshot)  # 이미지를 numpy 배열로 변환
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 색상 형식 변환

        out.write(frame)  # 프레임을 비디오 파일에 쓰기

        # 녹화 중지 조건 (여기서는 사용자가 키를 누를 때까지 계속 녹화)
        if cv2.waitKey(1) == ord('q'):  # 'q' 키를 누르면 녹화 중지
            break

    # 자원 해제
    out.release()
    cv2.destroyAllWindows()

# 사용 예: Notepad 윈도우 녹화 (Notepad 윈도우가 열려있어야 함)
record_window('Notepad')
