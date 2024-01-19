import os
import shutil

# 정리할 폴더 경로 설정 (예시로 download 폴더)
folder_path = 'C:\\Users\\김영호\\Downloads\\'

# 해당 폴더로 이동
os.chdir(folder_path)

# 폴더 내 모든 파일을 순회하며 작업 수행
for file in os.listdir(folder_path):
    # 파일 확장자 추출
    extension = file.split('.')[-1]

    # 확장자별 폴더 생성 및 파일 이동
    if os.path.isfile(file):
        # 대상 폴더 경로 설정
        directory = os.path.join(folder_path, extension)
        
        # 대상 폴더가 없으면 생성
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # 파일을 해당 확장자 폴더로 이동
        shutil.move(file, os.path.join(directory, file))