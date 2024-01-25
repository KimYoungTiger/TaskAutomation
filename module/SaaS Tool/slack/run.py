from translate import Translator
import requests
from requests.structures import CaseInsensitiveDict
import os
import json
import openai
import slack_sdk
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import time

# slack Message 보내기
def send_Slack_Message(input_message):
    
    # Token
    slack_token = ""
    client = WebClient(token=slack_token)

    # 보낼 다이렉트 메시지의 수신자 ID
    # user_id = "U055BHSUWAK" # 김영호 ID
    # print(user_id)
    
    # 메세지 보내기
    message = input_message
    response = client.chat_postMessage(channel=user_id, text=message)
    
    # 결과 확인
    if response["ok"]:
        print("Direct message sent successfully.")
    else:
        print(f"Failed to send direct message: {response['error']}")

# slack Message 가져오기
def get_slack_message():
    
    # Token
    slack_token = ""
    client = WebClient(token=slack_token)
    
    # 대화 내용을 가져올 채널 ID 설정
    channel_id = '' # imagecreate 채널

    # 대화 내용 가져오기
    response = client.conversations_history(channel=channel_id)

    global user_id
    
    if response['ok']:
        messages = response['messages']
        
        # print(message['text'] for message in messages if message['text'] == '<@U057QDU2PJS>*')
        # print(messages[0])
        user_id = messages[0]['user']
        
        if '@U057QDU2PJS' and '그려줘' in messages[0]['text']:
            # print(messages[0]['text'])
            slack_message = messages[0]['text'][15:].replace('그려줘','')
            return slack_message
        else:
            return ''
        
        # for message in messages:
        #     if '@U057QDU2PJS' and '그려줘' in message['text']:
        #         print(message['text'])
        #         slack_message = message['text'][15:].replace('그려줘','')
        #         break
            
    else:
        print('대화 내용을 가져올 수 없습니다.')

    # slack_message = "화창한 풍경"
    return slack_message

# service
def get_services():
    """Return the list of service names"""
    services = []
    for env_var in os.environ:
        if env_var.startswith("OPENAI_"):
            service_name = env_var[len("OPENAI_"):].lower()
            services.append(service_name)
    return services

# 이미지 생성
def generate_image(prompt):
    endpoint = "https://api.openai.com/v1/images/generations"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    api_key = "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"
    headers["Authorization"] = f"Bearer {api_key}"

    data = """
    {
        """
    data += f'"model": "image-alpha-001",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"512x512",
        "response_format":"url"
    }
    """

    resp = requests.post(endpoint, headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image")

    response_text = json.loads(resp.text)
    return response_text['data'][0]['url']


if __name__ == '__main__':
    
    # 슬렉에서 메세지 가져오기 (+한국어로 왔을경우 영어로 번역)
    translator = Translator(from_lang="ko",to_lang="en")
    pre_message = 'start'

    while True:
        
        now_message = get_slack_message()
        
        # print('now_message:' + now_message)
        # print('pre_message:'+ pre_message)
        
        if now_message != '' and now_message != pre_message:
            # print(translation)
            if pre_message != 'start':
                translation = translator.translate(now_message)
                image_url = generate_image(translation)
                send_Slack_Message(image_url)
            
            # 루프 확인용
            pre_message = now_message
            
        time.sleep(10)
        print('실시간 감지중')
            
    # translation = translator.translate(get_slack_message())
    
    # # 이미지 생성
    # image_url = generate_image(translation)

    # # 이미지 URL 슬렉에 메세지로 보내기
    # send_Slack_Message(image_url)


