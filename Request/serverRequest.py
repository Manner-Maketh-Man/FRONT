import requests
import json
import Request.ClovaApiConnection as ClovaApiConnection

def send_request():
    # 서버 URL
    url = 'https://aca8-1-210-216-4.ngrok-free.app/apis/process_json/'

    # 함수 호출
    image_file = 'ScreenShot_img/IMGforOCR.jpg'
    OCR_response = ClovaApiConnection.send_OCR_request(image_file)
    
    # 데이터를 필요 시 JSON 형식으로 변환
    json_data = OCR_response.json()
    
    # 보낼 데이터
    # data = {}

    # 요청 헤더 정의 (JSON 형식의 데이터를 보내기 때문에 'Content-Type'을 'application/json'으로 설정)
    headers = {'Content-Type': 'application/json'}

    # POST 요청
    response = requests.post(url, data=json.dumps(json_data), headers=headers)

    # 응답 출력 (JSON 형식일 경우)
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        return response_data
    else:
        print("Error:", response.status_code)

# 함수 호출
send_request()
