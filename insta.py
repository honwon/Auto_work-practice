from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from myID import ID, PW
from time import sleep


driver = webdriver.Chrome("./chromedriver")

try:
    driver.get("https://www.instagram.com")

    # 링크 텍스트가 로그인인것을 받아옴
    # elem = driver.find_element_by_link_text("로그인")
    # 클릭
    # elem.click()
    
    # 잠시 1초 동안 기다려라
    sleep(1)
    
    # name 값으로 찾음
    elem = driver.find_element_by_name("username")
    # 아이디 입력
    elem.send_keys(ID)

    elem = driver.find_element_by_name("password")
    # 비밀번호 입력
    elem.send_keys(PW)
    # 엔터

    elem.send_keys(Keys.RETURN)

    # 1번쨰 알림창 나중에 하기 선택
    sleep(3)
    elem = driver.find_element_by_class_name('sqdOP')
    elem.click()

    # 2번쨰 알림창 나중에 하기 선택
    sleep(3)
    # elem = driver.find_element_by_css_selector('button.aOOlW.HoLwm')
    elem = driver.find_element_by_class_name("HoLwm")
    elem.click()

    sleep(2)

    # input에 넣는 방법
    # elem = driver.find_element_by_class_name("XTCLo")
    # elem.send_keys("#travel")
    # elem.send_keys(Keys.RETURN)
    # elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_class_name("XTCLo")
    elem.send_keys("#패스트캠퍼스")

    sleep(2)
    # 동작을 체인처럼 연결함 ac.은 등록하는 과정
    ac = ActionChains(driver)
    # 마우스가 그 위치로 이동
    ac.move_to_element(elem)
    # 키를 누름
    ac.click()
    # 앞에서 등록한 모든 동작을 실행한다.
    # ac.perform()
    # 앞에서 취했던 동작 모두 초기화
    # ac.reset_actions()
    # 현 위치에서 좌표 설정대로 움직임
    ac.move_by_offset(0,50)
    ac.click()
    ac.perform()


except Exception as e:
    print(e)
finally:
    print("\n종료")
    # driver.quit()

