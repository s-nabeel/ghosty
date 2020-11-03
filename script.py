import pyautogui
import time
pyautogui.FAILSAFE = False

while True:
    # How many seconds before ghosty.py starts
    time.sleep(10)
    for i in range(0, 100):
        pyautogui.moveTo(0, i * 5)
        print('Cursor moved')
        # Sleep for 300 seconds (5 minutes) after each time the cursor is moved
        time.sleep(10)
    # for i in range(0, 5)