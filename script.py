import pyautogui
import random
import time
pyautogui.FAILSAFE = False

while True:
    # How many seconds after ghosty.py is ran should the script start
    time.sleep(10)
    for i in range(0, 2):
        pyautogui.moveTo(0, i * 5)
        print("Cursor moved")
        # Sleep for 300 seconds (5 minutes) after each time the cursor is moved
        time.sleep(10)
    for i in range(0, 1):
        sentences = ["Please excuse me for a moment", "BRB, my package from Amazon just arrived",
                     "BRB, just making some coffee"]
        pyautogui.write(random.choice(sentences))
        pyautogui.press('enter')
        print("Message typed")