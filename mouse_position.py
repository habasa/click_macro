import pyautogui

print("마우스를 움직이면 현재 좌표가 표시됩니다. 중지하려면 Ctrl+C를 누르세요.")

try:
    while True:
        x, y = pyautogui.position()  # 현재 마우스 위치 가져오기
        print(f"X: {x}, Y: {y}", end="\r")  # 실시간으로 좌표 표시
except KeyboardInterrupt:
    print("\n좌표 확인을 중지합니다.")
