import time
import pyautogui

loginmode = input("google login on/off:")
code = input("code:")
name = "random"
setnum = input("how many:")
num = 0
short = 0.5
middle = 1
long = 3

names = ["Jacob", "Emma", "Daniel", "Kamal", "Krishna", "Aiden", "George", "Logan", "nolan", "andrew", "liam", "david", "Linus", "paul", "daniel"]

if name == "random":
    name = "nolan"
    ran = True


def logoff():
    pyautogui.press("winleft")
    time.sleep(short)
    pyautogui.write("google")
    time.sleep(middle)
    pyautogui.write("kahoot.it")
    pyautogui.press("enter")
    time.sleep(short)
    pyautogui.press("f11")
    time.sleep(long)
    pyautogui.moveTo(971, 575)
    pyautogui.click()
    pyautogui.write(code)
    pyautogui.press("enter")
    time.sleep(middle)
    pyautogui.moveTo(971, 600)
    pyautogui.click()
    pyautogui.typewrite(name, interval=0.3)
    pyautogui.press("enter")


def logon():
        pyautogui.press("winleft")
        time.sleep(short)
        pyautogui.write("google")
        time.sleep(short)
        pyautogui.press("enter")
        time.sleep(long)
        pyautogui.press("f11")
        time.sleep(short)
        pyautogui.moveTo(113, 1022)
        pyautogui.click()
        pyautogui.write("kahoot.it")
        pyautogui.press("enter")
        time.sleep(short)
        pyautogui.press("f11")
        time.sleep(long)
        pyautogui.moveTo(971, 575)
        pyautogui.click()
        pyautogui.write(code)
        pyautogui.press("enter")
        time.sleep(middle)
        pyautogui.moveTo(971, 600)
        pyautogui.click()
        pyautogui.typewrite(name, interval=0.3)
        pyautogui.press("enter")

def repeat():
    if ran == True:
        name = names[num]

    time.sleep(middle)
    pyautogui.press("f11")
    time.sleep(long)
    pyautogui.keyDown("ctrl")
    pyautogui.press("t")
    pyautogui.keyUp("ctrl")
    time.sleep(middle)
    pyautogui.write("kahoot.it")
    pyautogui.press("enter")
    time.sleep(short)
    pyautogui.press("f11")
    time.sleep(long)
    pyautogui.moveTo(971, 575)
    pyautogui.click()
    pyautogui.write(code)
    pyautogui.press("enter")
    time.sleep(long)
    pyautogui.moveTo(971, 588)
    pyautogui.click()
    pyautogui.typewrite(name, interval=0.3)
    pyautogui.press("enter")

setnum = int(setnum)

while setnum > num:
    if num == 0:
        if loginmode == "off":
            logoff()
        elif loginmode == "on":
            logon()
    repeat()
    num += 1



