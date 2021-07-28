import pyautogui
import datetime
import time
import os
# import asyncio


def captureSave(pathDir,count):
    dateNow = datetime.datetime.now()
    # print(dateNow)
    filename = f"{count}_{dateNow.strftime('%Y-%m-%d %H%M%S.%f')}"
    
    pyautogui.screenshot().save(f"{pathDir}\\{filename}.png")    

def main(sleepTime):
    pathDirScreenshot = f"{os.path.dirname(os.path.abspath(__file__))}\\screenshot"

    if not os.path.exists(pathDirScreenshot):
        os.makedirs(pathDirScreenshot)

    for count in range (0,180):
        time.sleep(sleepTime)
        captureSave(pathDirScreenshot,count)

if __name__ == "__main__":
    print(__name__)
    main(60)
else:
    print(__name__)

    


