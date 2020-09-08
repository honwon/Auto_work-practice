from selenium import webdriver

# 파이썬 폴덩 ㅏㄴ의 크롬드라이버
driver = webdriver.Chrome("./chromedriver")

try:
    # 네이버 뉴스로 이동 get은 주소로 이동해달라
    driver.get("https://news.naver.com")
    
    # element 안의 div id 불러옴
    elem = driver.find_element_by_id("right.ranking_contents")
    # 텍스트 추출
    # print(elem.text)

    # elements - 복수가 되면 다 들고옴 for 사용
    lis = elem.find_elements_by_tag_name("li")

    for li in lis:
        # element가 단수면 하나만 들고옴
        atag = li.find_element_by_tag_name("a")
        print(atag.text)

except Exception as e:
    print(e)
    
finally:
    driver.quit()