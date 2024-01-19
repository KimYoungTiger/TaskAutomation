import cv2
import numpy as np
import pyautogui
import tkinter as tk
from threading import Thread
from datetime import datetime  # 날짜와 시간을 위한 모듈
from tkinter import messagebox

class ScreenRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Recording")
        self.is_recording = False
        self.screen_size = pyautogui.size()
        self.codec = cv2.VideoWriter_fourcc(*'XVID')
        self.output = None  # 초기 비디오 라이터는 None으로 설정
        
        # 창 크기와 위치 설정
        window_width = 250
        window_height = 100
        
        # # 스크린 너비와 높이 구하기
        # screen_width = self.root.winfo_screenwidth()
        # screen_height = self.root.winfo_screenheight()
        
        # # 창을 화면 가운데에 위치시키기 위한 x, y 좌표
        # center_x = int((screen_width/2) - (window_width/2))
        # center_y = int((screen_height/2) - (window_height/2))
        
        # self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.root.geometry(f'{window_width}x{window_height}')
                           
        # self.root.resizable(False, False)  # 창 크기 조정 불가능하도록 설정

        
        # GUI 설정
        self.start_button = tk.Button(root, text='Start Recording', command=self.start_recording)
        self.start_button.pack()
        
        self.stop_button = tk.Button(root, text='Stop Recording', command=self.stop_recording)
        self.stop_button.pack()
        
    def get_filename(self):
        # 현재 날짜와 시간을 기반으로 파일 이름 생성
        now = datetime.now()  # 현재 날짜와 시간
        return now.strftime('%Y%m%d_%H%M%S.avi')  # 'YYYYMMDD_HHMMSS.avi' 형식으로 반환

    def record_screen(self):
        # 실제 화면 녹화를 수행하는 함수
        while self.is_recording:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.output.write(frame)
        # 녹화가 중지되면 비디오 파일을 닫음
        self.output.release()

    def start_recording(self):
        # 녹화를 시작하는 함수
        if not self.is_recording:
            self.is_recording = True
            # 새 녹화 세션을 위한 파일 이름 가져오기
            filename = self.get_filename()
            # 비디오 라이터 설정
            self.output = cv2.VideoWriter(filename, self.codec, 20.0, self.screen_size)
            # record_screen 함수를 별도의 스레드에서 실행
            Thread(target=self.record_screen).start()

    def stop_recording(self):
        # 녹화를 중지하는 함수
        if self.is_recording:
            self.is_recording = False
            # 녹화 완료 메시지 표시
            messagebox.showinfo("알림", "녹화가 완료되었습니다!")
            
    def on_closing(self):
        # 프로그램 종료 시 호출되는 함수
        self.stop_recording()  # 녹화 중지
        self.root.destroy()  # GUI 창 닫기

# 메인 함수
if __name__ == "__main__":
    root = tk.Tk()  # 메인 윈도우 생성
    recorder = ScreenRecorder(root)  # ScreenRecorder 인스턴스 생성
    root.protocol("WM_DELETE_WINDOW", recorder.on_closing)  # 창 닫기 버튼 설정
    root.mainloop()  # Tkinter 이벤트 루프 실행
