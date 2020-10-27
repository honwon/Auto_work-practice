import pyautogui
import time
# 프로그램을 관리하는 ㅍ키지
import subprocess

# call 함수를 쓰면 끝나기 전까지 대기하게 된다 

# 맥
# kakao = subprocess.Popen(['open','-a','KakaoTalk'])
# 윈도우 역슬래시 2개를 입력해야한다
kakao = subprocess.Popen(["C:\\Program Files (x86)\\Kakao\\KakaoTalk\\KakaoTalk.exe"])
time.sleep(3)


# pyautogui.typewrite(ID)
# pyautogui.press("tab")
# pyautogui.typewrite(PW)
# pyautogui.press("enter")

time.sleep(2)

x,y = pyautogui.locateCenterOnScreen("profile.png")
# 더블클릭
pyautogui.click(x,y,2)

time.sleep(3)

pyautogui.typewrite("test message")
pyautogui.press("enter")
