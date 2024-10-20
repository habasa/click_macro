import pyautogui
import time
import keyboard

def click_at_position(x, y, interval):
    while True:
        if keyboard.is_pressed('q'):  # 'q' 키를 누르면 중지
            print("클릭 매크로 중지됨!")
            break
        pyautogui.click(x=x, y=y)
        print(f"Clicked at position ({x}, {y})")
        time.sleep(interval)

print("매크로 실행 중... 중지하려면 'q' 키를 누르세요.")
click_at_position(400, 500, 0.0001)
