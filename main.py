# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, sys, os
import win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def pickUp():
    keyboard.press('z')
    time.sleep(0.5)
    keyboard.release('z')

def attack(x,y):
    click(x, y)
    sleep(4)
    keyboard.press('space')
    sleep(1)
    while pyautogui.locateOnScreen('piatragasita.png', region=(568,68,150,30), grayscale=False, confidence=.5):
        keyboard.press('space')
    pickUp()
    if pyautogui.locateOnScreen('piatra.png', region=(122, 121, 1029, 575), grayscale=True, confidence=.5):
            c = pyautogui.locateOnScreen('piatra.png', region=(122, 121, 1029, 575), grayscale=True, confidence=.5)
            global xA
            global yA
            xA, yA = pyautogui.center(c)
            print(xA, yA)
            attack(xA, yA)
    else:
        keyboard.release('space')
        findStone()
    print("Ultima piatra distrusa a fost la %s:%s" % (x, y))

def findStone():
        if pyautogui.locateOnScreen('piatra.png',region=(122,121,1029,575), grayscale=True, confidence=.5):
            c = pyautogui.locateOnScreen('piatra.png', region=(122,121,1029,575), grayscale=True, confidence=.5)
            global x
            global y
            x, y = pyautogui.center(c)
            print(x,y)
            return True;

def lookAround():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    pyautogui.moveRel(20, 0)
    if findStone() == True:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        print ('Gasit si urmeaza sa atac:'+ str(x) +' ' + str(y))
        attack(x,y)
    elif findStone() == False:
        lookAround()


while keyboard.is_pressed('q') == False:
    # print (str(x) +'' +str(y))
    sleep(1)
    lookAround()

# while keyboard.is_pressed('q') == False:
#     if pyautogui.locateOnScreen('piatra.png',region=(4,32,1293,689), grayscale=False, confidence=.5):
#         sleep(10)
#         #leftClick(pyautogui.locateOnScreen('piatra.png', region=(4,32,1293,689), grayscale=False, confidence=.5))
#         #doubleClick(pyautogui.locateOnScreen('piatra.png', region=(4,32,1293,689), grayscale=False, confidence=.5))
#         c = pyautogui.locateOnScreen('piatra.png', region=(4,32,1293,689), grayscale=False, confidence=.5)
#         x,y= pyautogui.center(c)
#         print(x,y)
#         click(x,y)
#         sleep(5)
#         attack()


