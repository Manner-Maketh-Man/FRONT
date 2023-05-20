import os
import pyautogui

def capture_screenshot(screenshot_directory="ScreenShot_img", screenshot_file="IMGforOCR.jpg"):
    # 스크린샷을 저장할 폴더 경로
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory)

    # 스크린샷 파일 경로 설정
    screenshot_path = os.path.join(screenshot_directory, screenshot_file)

    # 스크린샷 캡처 후 이미지 모드를 RGB로 변환하여 저장
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert("RGB")

    # 기존의 스크린샷 파일이 있으면 삭제
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    # 새로운 스크린샷 저장
    screenshot.save(screenshot_path)
