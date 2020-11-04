import pyautogui
import random
import sys
import time
import datetime

pyautogui.FAILSAFE = False

while True:
    now = datetime.datetime.now()
    print("ghosty started at: " + now.strftime("%H:%M:%S on %m-%d-%Y"))

    # How many seconds after ghosty.py is ran should the script start
    time.sleep(10)
    for i in range(0, 10):
        pyautogui.moveTo(0, i * 5)
        print("\nCursor moved")

        def countdown(t):
            while t >= 0:
                sys.stdout.write("\rTime elapsed: {}s ".format(t))
                t -= 1
                sys.stdout.flush()
                time.sleep(1)
        # Sleep for 300 seconds (5 minutes) after each time the cursor is moved
        # 300 seconds = 50 minutes of cursor movement before typing a message
        countdown(300)

    for i in range(0, 1):
        sentences = ["Please excuse me for a moment", "BRB, my package from Amazon just arrived",
                     "BRB, just making some coffee"]
        pyautogui.write(random.choice(sentences))
        pyautogui.press('enter')
        print("Message typed")