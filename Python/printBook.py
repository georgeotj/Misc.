# This script was used on a 3440x1440 monitor. To be able to properly use the pyautogui module please refer to the documentation.
import pyautogui
import time
chapter = 10
pages = 37


def printPage():
    #Hover over the print symbol
    pyautogui.moveTo(1565, 190, duration=0.15)
    pyautogui.click()
    pyautogui.click()

    #Click on the secondary print button
    time.sleep(.8)
    pyautogui.click()

    # #Print to PDF
    pyautogui.moveTo(1565, 190, duration=0.15)
    time.sleep(.5)
    pyautogui.click()
    pyautogui.moveTo(1580, 520, duration=0.15)
    pyautogui.click()
    pyautogui.moveTo(1580, 550, duration=0.15)
    pyautogui.click()

    #Name the PDF
    pyautogui.typewrite(pdfName)
    pyautogui.press('enter')
    time.sleep(.75)
    pyautogui.moveTo(1640,160, duration=.15)
    pyautogui.click()
    time.sleep(.8)

    #Go to next page
    pyautogui.moveTo(1636, 840, duration=0.15)
    pyautogui.click()
    time.sleep(.8)

for i in range(pages):
    pdfName = "FoundationsOfMarketing_Ch"+str(chapter)+"_Pg"+str(i+1)
    printPage()
