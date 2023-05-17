import os
import time
import pyautogui

# 스크린샷을 저장할 폴더 경로
screenshot_directory = "ScreenShot_img"
if not os.path.exists(screenshot_directory):
    os.makedirs(screenshot_directory)

interval = 5  # 스크린샷 간격(초)

# 스크린샷 파일 경로 설정
screenshot_path = os.path.join(screenshot_directory, "IMG.jpg")

while True:
    current_time = time.time()

    # 스크린샷 캡처 후 이미지 모드를 RGB로 변환하여 저장
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert("RGB")

    # 기존의 스크린샷 파일이 있으면 삭제
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    # 새로운 스크린샷 저장
    screenshot.save(screenshot_path)

    # 다음 스크린샷을 위해 일정 시간 동안 대기
    time.sleep(interval)