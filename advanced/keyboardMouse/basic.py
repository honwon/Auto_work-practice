import pyautogui

# 마우스 이동 
pyautogui.moveTo(0,0)
# 현재 마우스 위치로부터 이동
pyautogui.moveRel(0,0)

# 지정한 포지션 클릭 비어있으면 현재 포지션 클릭
pyautogui.click(800,0)

# 글자 입력
pyautogui.typewrite("abce")

# 지정한 키보드 명령 입력
pyautogui.press("enter")

#스크린샷 찍기
pyautogui.screenshot("result.png")

