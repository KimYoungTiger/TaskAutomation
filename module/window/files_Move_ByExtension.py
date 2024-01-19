import os
import shutil

def move_files_with_extension(source_directory, destination_directory, extension):
    # 소스 디렉토리에서 파일 목록 가져오기
    files = os.listdir(source_directory)

    # 특정 확장자를 가진 파일들만 이동
    for file in files:
        if file.endswith(extension):
            shutil.move(os.path.join(source_directory, file), 
                        os.path.join(destination_directory, file))

# 사용 예시
source_directory = 'path/to/source/directory'
destination_directory = 'path/to/destination/directory'
extension = '.txt'

move_files_with_extension(source_directory, destination_directory, extension)
