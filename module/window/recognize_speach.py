import speech_recognition as sr

# 음성을 입력받기 위한 Recognizer 객체 생성
r = sr.Recognizer()

# 마이크로부터 오디오를 읽어들이는 함수
def record_audio():
    with sr.Microphone() as source:
        print("음성을 입력하세요:")
        audio = r.listen(source)
    return audio

# 음성을 텍스트로 변환하는 함수
def recognize_speech(audio):
    try:
        text = r.recognize_google(audio, language='ko-KR')  # Google 음성 인식 엔진 사용, 한국어 설정
        print("인식된 텍스트:")
        print(text)
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
    except sr.RequestError as e:
        print(f"음성 인식 서비스에서 오류가 발생했습니다: {e}")

# 음성 입력받고 변환 실행
audio_input = record_audio()
recognize_speech(audio_input)

