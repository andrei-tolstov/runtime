#! /usr/bin/python3
#pip install pyautogui

import pyautogui
import time

file = "D:\\VScodeWorkSpace\\070824\\-\\dins.txt"

user = "admin"
ips = []

with open(str(file), "r",  encoding="utf8") as list0:
    for line in list0.readlines():
        ips0 = list(line.strip('\n').split(" "))
        ips = ips + ips0

print(ips)

def click(x, y , wrt):
    pyautogui.moveTo(x, y)
    pyautogui.click() 
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    pyautogui.write(wrt)

def mvcl(x, y, sl):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(sl)


for t in ips:
    print(str(ips.index(t)) + " / " + str(len(ips)))
    click(812, 76, t)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(973, 535)
    pyautogui.click()
    pyautogui.moveTo(976, 804)
    pyautogui.click()
    time.sleep(3)
    click(950, 450, user)
    click(937, 491, user)
    mvcl(955, 599, 3)
    mvcl(918, 182, 3)
    mvcl(105, 329, 3)
    mvcl(928, 765, 5)
    click(922, 409, "http://msk-co-yealink.ivoin.ru/$PN")
    mvcl(947, 609, 1)
    mvcl(926, 722, 1)
    click(914, 708, "60")
    mvcl(552, 949, 5)
    mvcl(918, 886, 3)
    mvcl(1060, 231, 1)

