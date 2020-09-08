from selenium import webdriver
# 앤터나 방향키 사용 가능
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")


try:
    driver.get("https://naver.com")

    # 검색창 아이디 불러오기 보통 아이디는 고유하다 아이디는 바로 사용하면 된다.
    elem = driver.find_element_by_id("query")

    # 검색창에 키 전달
    elem.send_keys("패스트캠퍼스")
    # 엔터키?
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_class_name("_blogBase")

    # lis = elem.find_elements_by_class_name("sh_blog_title")
    # for i in lis:
    #     print(i.text)
    
    li = elem.find_elements_by_tag_name("li")
    for l in li:
        atag = l.find_element_by_class_name("sh_blog_title")

        # get_attribute는 속성값을 들고온다
        print(atag.get_attribute("title"))
        # 링크를 들고오는 속성값
        print(atag.get_attribute("href"))
        print(atag.get_attribute("text"))
        print(atag.get_attribute("target"))
        print(atag.get_attribute("class"))

except Exception as e:
    print(e)

finally:
    print("final")
    # driver.quit()