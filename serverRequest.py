import requests
import json

# 서버 URL
url = 'https://c774-211-198-109-254.ngrok-free.app/apis/process_file/'

# 보낼 데이터
data = {}

# 데이터를 JSON 형식으로 변환
json_data = json.dumps(data)

# 요청 헤더 정의 (JSON 형식의 데이터를 보내기 때문에 'Content-Type'을 'application/json'으로 설정)
headers = {'Content-Type': 'application/json'}

# POST 요청
response = requests.post(url, data=json_data, headers=headers)

# 응답 출력 (JSON 형식일 경우)
if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print("Error:", response.status_code)