from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

try:
    # 네이버 뉴스로 이동 get은 주소로 이동해달라
    driver.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blMy&qvt=0&query=%EC%82%AC%EB%9E%91%20%EB%AA%85%EC%96%B8")
    
    # element 안의 div id 불러옴
    elem = dirver.find_elements_by_class_name("lngkr")
    # 텍스트 추출
    print(elem.text)

except Exception as e:
    print(e)
    
finally:
    driver.quit()