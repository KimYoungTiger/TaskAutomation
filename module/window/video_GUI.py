import cv2  # OpenCV 라이브러리 임포트
import tkinter as tk  # Tkinter GUI 라이브러리 임포트
from threading import Thread  # 스레딩 모듈에서 Thread 클래스 임포트

class VideoRecorder:
    def __init__(self, root):
        self.root = root  # 메인 윈도우 (root) 인스턴스
        self.capture = cv2.VideoCapture(0)  # 웹캠 초기화 (0은 일반적으로 기본 웹캠을 의미함)
        self.is_recording = False  # 녹화 상태 플래그
        self.out = None  # 비디오 파일을 위한 변수

        # 녹화 시작 버튼 생성 및 배치
        self.start_button = tk.Button(root, text='Start Recording', command=self.start_recording)
        self.start_button.pack()
        
        # 녹화 정지 버튼 생성 및 배치
        self.stop_button = tk.Button(root, text='Stop Recording', command=self.stop_recording)
        self.stop_button.pack()

    def start_recording(self):
        # 녹화 시작 함수
        if not self.is_recording:
            self.is_recording = True  # 녹화 상태를 True로 설정
            # 비디오 파일 저장을 위한 설정 (파일명, 코덱, FPS, 해상도)
            self.out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
            # 녹화를 수행하는 별도의 스레드 시작
            Thread(target=self.record).start()

    def stop_recording(self):
        # 녹화 정지 함수
        if self.is_recording:
            self.is_recording = False  # 녹화 상태를 False로 설정

    def record(self):
        # 실제 녹화를 수행하는 함수
        while self.is_recording:
            ret, frame = self.capture.read()  # 카메라로부터 프레임 읽기
            if ret:
                self.out.write(frame)  # 프레임을 비디오 파일에 쓰기
            else:
                break  # 카메라로부터 프레임을 읽는 데 실패하면 종료

    def on_closing(self):
        # 프로그램 종료 시 호출되는 함수
        self.stop_recording()  # 녹화 중지
        self.capture.release()  # 카메라 리소스 해제
        self.out.release()  # 비디오 파일 해제
        self.root.destroy()  # GUI 창 닫기

if __name__ == "__main__":
    root = tk.Tk()  # 메인 윈도우 생성
    recorder = VideoRecorder(root)  # VideoRecorder 인스턴스 생성
    root.protocol("WM_DELETE_WINDOW", recorder.on_closing)  # 창 닫기 버튼 누를 때 on_closing 함수 호출 설정
    root.mainloop()  # Tkinter 이벤트 루프 실행
