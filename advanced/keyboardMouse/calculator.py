import pyautogui
from time import sleep


pyautogui.click(300,150)

# 이미지를 가지고 위치를 찾아 클릭한다 검은 이미지는 잘 안되나?
x, y = pyautogui.locateCenterOnScreen('1.png')
pyautogui.click(x,y)

x, y = pyautogui.locateCenterOnScreen("3.png")
pyautogui.click(x,y)

x, y = pyautogui.locateCenterOnScreen("+.png")
pyautogui.click(x,y)

pyautogui.press("enter")
