import requests
import json
import Request.ClovaApiConnection as ClovaApiConnection

# import time

def send_request():
    # 시작시간
    # start = time.time()
    
    # 서버 URL
    url = 'https://aca8-1-210-216-4.ngrok-free.app/apis/process_json/'

    # 함수 호출
    image_file = 'ScreenShot_img/IMGforOCR.jpg'
    OCR_response = ClovaApiConnection.send_OCR_request(image_file)
    
    # OCR 종료시간
    # OCRend = time.time()
    # print('Clova OCR reponse에 걸린 시간 :',OCRend - start,'sec')
    
    # 데이터를 필요 시 JSON 형식으로 변환
    json_data = OCR_response.json()
    print('Clova OCR 결과 : ',json_data)
    # json_data를 .json 파일로 저장
    with open('ScreenShot_img/data.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
        print("JSON 파일이 성공적으로 저장되었습니다.")

    # 요청 헤더 정의 (JSON 형식의 데이터를 보내기 때문에 'Content-Type'을 'application/json'으로 설정)
    headers = {'Content-Type': 'application/json'}

    # POST 요청
    response = requests.post(url, data=json.dumps(json_data), headers=headers)

    # 응답 출력 (JSON 형식일 경우)
    if response.status_code == 200:
        response_data = response.json()
        print('Server Response data:',response_data)
        # 종료시간
        # end = time.time()
        # print('Server reponse에 걸린 시간 :',end - start,'sec')
        return response_data
    else:
        print("Error:", response.status_code)

# for debug
# send_request()