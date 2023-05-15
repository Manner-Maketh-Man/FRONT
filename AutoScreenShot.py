# import time # 스크린샷 시간 간격이 필요하다면 추가한다.

import pyautogui

num = 1

while True:

    pyautogui.screenshot(f'/ScreenShot_img/img_{str(num).zfill(4)}.png', region=(10, 200, 1000, 1800))

    # time.sleep(1) # 스크린샷 시간 간격이 필요하다면 추가한다. 1은 초이다.

    pyautogui.press('right')

    num += 1