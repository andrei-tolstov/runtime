
import pyautogui
import time

file = "D:\\VScodeWorkSpace\\070824\\-\\yealink_in.txt"

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
    time.sleep(20)
    mvcl(932, 663, 0.5)
    mvcl(917, 775, 0.5)
    click(941, 598, user)
    click(941, 630, user)
    pyautogui.press('enter')
    time.sleep(60)
    mvcl(1015, 255, 3)
    mvcl(801, 615, 0.5)
    pyautogui.press('pagedown')
    time.sleep(0.5)
    pyautogui.press('pagedown')
    time.sleep(0.5)
    mvcl(604, 771, 0.5)
    pyautogui.press('pagedown')
    time.sleep(0.5)
    pyautogui.press('pagedown')
    time.sleep(0.5)
    click(900, 648, "msk-co-yealink.ivoin.ru/X1S")
    mvcl(822, 703, 0.5)
    mvcl(812, 764, 0.5)
    mvcl(836, 767, 0.5)
    mvcl(834, 828, 0.5)
    mvcl(734, 892, 1)
    mvcl(493, 809, 1)
    mvcl(856, 810, 1)



    # mvcl(849, 238, 3)
    # mvcl(697, 410, 0.5)
    # mvcl(1024, 596, 2)
    # pyautogui.press('pagedown')
    # pyautogui.press('pagedown')
    # time.sleep(2)
    # mvcl(761, 962, 1)
    # mvcl(1055, 286, 1)