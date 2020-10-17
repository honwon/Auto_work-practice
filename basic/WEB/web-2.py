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

    print("BLOG")
    for l in li :
        atag = l.find_element_by_class_name("sh_blog_title")

        # get_attribute는 속성값을 들고온다
        print(atag.get_attribute("title"))
        # 링크를 들고오는 속성값
        print(atag.get_attribute("href"))

    print("-"*20)
    elemNews = driver.find_element_by_class_name("_prs_nws_all")
    # 위 코드에 대해 경로 설정
    newLi = elemNews.find_elements_by_xpath("./ul/li")

    print("NEWS")
    for i in newLi:
        # 에러가 났었던 이유 = 하위에 li tag가 더 있었음
        atag = i.find_element_by_class_name("_sp_each_title")
        print(atag.get_attribute("title"))
        print(atag.get_attribute("href"))

    print("-"*20)

    elemCafe = driver.find_element_by_class_name("_cafeBase")
    # 위 코드에 대해 경로 설정
    cafeLi = elemCafe.find_elements_by_xpath("./ul/li")

    print("CAFE")
    for i in cafeLi:
        # 에러가 났었던 이유 = 하위에 li tag가 더 있었음
        atag = i.find_element_by_class_name("sh_cafe_title")
        #타이틀에 내용이 있으면 그대로 아니면 text정보를 넣어주세용
        title = atag.get_attribute("title")
        if not title:
            title = atag.text
        
        print(title)
        print(atag.get_attribute("href"))

except Exception as e:
    print(e)

finally:
    print("\n끝")
    # driver.quit()