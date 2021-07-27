import pyautogui
import datetime
import time
import os

pathScreenshot = f"{os.path.dirname(os.path.abspath(__file__))}\\screenshot"

if not os.path.exists(pathScreenshot):
            os.makedirs(pathScreenshot)

for count in range (0,180):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f"{pathScreenshot}\\{count}_{datetime.datetime.now().strftime('%Y-%m-%d %H%M%S.%f')}.png")
    time.sleep(60)