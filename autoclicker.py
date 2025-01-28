import pyautogui
import time
import keyboard

def click_at_positions(positions, click_pattern, interval):
    while True:
        if keyboard.is_pressed('q'):  # 'q' 매크로 정지
            print("클릭 매크로 중지됨!")
            break

        for i, (x, y) in enumerate(positions):
            clicks = click_pattern[i]  # 해당 좌표에서 클릭할 횟수
            for _ in range(clicks):
                pyautogui.click(x=x, y=y)
                print(f"Clicked at position ({x}, {y})")
                time.sleep(interval)

print("매크로 실행 중... 중지하려면 'q' 키를 누르세요.")
# 클릭할 좌표와 각 좌표의 클릭 횟수
click_positions = [(469, 500), (723, 390)]
click_pattern = [10, 1]  # (469, 500)에서 10번 클릭 후 (723, 400)에서 1번 클릭

click_at_positions(click_positions, click_pattern, 0.01)
