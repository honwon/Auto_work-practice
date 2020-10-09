from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# 파이썬 폴덩 ㅏㄴ의 크롬드라이버
driver = webdriver.Chrome("./chromedriver")

try:
    # 네이버 뉴스로 이동 get은 주소로 이동해달라
    driver.get("https://www.jma.go.jp/en/g3/")
    
    elem = driver.find_element_by_class_name("pagelink")
    print(elem.text)

    pdf = elem.find_element_by_tag_name("a")
    pdf.click()


except Exception as e:
    print(e)
    
finally:
    print("finish")
