import requests
import uuid
import time
import base64
import json

api_url = 'https://6vscc0s85m.apigw.ntruss.com/custom/v1/22584/e850e8dee292beeaf2c81d10985825dff13bb57786964eee183fc68a522810d3/infer'
secret_key = 'Q2RYaGplQmhUaHpCbnlVWkVRZGlwaHVDeHJFVm5YY3A='
# image_url = ''

image_file = 'ScreenShot_img/IMGforOCR.jpg'
with open(image_file,'rb') as f:
    file_data = f.read()

request_json = {
    'images': [
        {
            'format': 'jpg',
            'name': 'demo',
            'data': base64.b64encode(file_data).decode(),
            # 'url': image_url
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}
payload = json.dumps(request_json).encode('UTF-8')
headers = {
  'X-OCR-SECRET': secret_key,
  'Content-Type': 'application/json'
}

response = requests.request("POST", api_url, headers=headers, data = payload)

print(response.text)