import pyautogui
import datetime
import time
import os

myScreenshot = pyautogui.screenshot()

for count in range (0,180):
    myScreenshot.save(f"{os.path.dirname(os.path.abspath(__file__))}\\screenshot\\{count}_{datetime.datetime.now().strftime('%Y-%m-%d %H%M%S.%f')}.png")
    time.sleep(60)