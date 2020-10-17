import time
import gspread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from oauth2client.service_account import ServiceAccountCredentials


driver = webdriver.Chrome("./chromedriver")

try:
    driver.get("https://cafe.naver.com/joonggonara")

    elem = driver.find_element_by_id("topLayerQueryInput")

    # 자전거 검색 후 엔터
    elem.send_keys("자전거")
    elem.send_keys(Keys.RETURN)

    #iframe 변수 설정
    iframe = driver.find_element_by_id("cafe_main")
    # iframe 태그 안으로 들어감
    driver.switch_to.frame(iframe)

    # 쓸 서비스 API 권한 얻기 []인 이유는 여러 권한을 얻을 수 있기 위함
    # 스프레드 시트 API , 드라이브 API 필요 = 시트생성 권한
    scope = [
        "https://www.googleapis.com/auth/drive",
        "https://spreadsheets.google.com/feeds"
        ]
    # 내 계정의 키, 사용할 API
    credentials = ServiceAccountCredentials.from_json_keyfile_name("cred.json",scope)
    # 인증 정보를 가지고 인증 시도
    gs = gspread.authorize(credentials)
    # 스프레드시트 생성
    doc = gs.create("중고나라 검색결과")
    # 데이터를 넣는 것과 공유는 순서 상관 없다.
    ws = doc.get_worksheet(0)

    curr_page = 1

    while True:
        elem = driver.find_element_by_xpath("//div[@class='article-board m-tcol-c'][2]")
        trs = elem.find_elements_by_xpath("./table/tbody/tr")

        for tr in trs:
            # 속성값 받아옴
            # if not tr.get_attribute("align"):
            #     continue
            
            # a 태그안 내용 분석
            # atag = tr.find_element_by_tag_name("a")
            atag = tr.find_element_by_xpath("./td/div[2]/div/a")
            # []안에 넣어야 함
            ws.append_row([atag.text])

        if curr_page==2:
            break
        curr_page += 1
        # a링크 텍스트를 검색 페이지
        page = driver.find_element_by_link_text(str(curr_page))
        page.click()

# 이메일 주소가 들어감 사용자 권한 설정 reader-읽기 전용, writer-쓰기 전용 소유자가 내가 아니면 공유 문서에서 확인 가능
    doc.share("moheom98@gmail.com",perm_type="user",role="owner")
    input()
except Exception as e:
    print(e)
finally:
    print("quit")

