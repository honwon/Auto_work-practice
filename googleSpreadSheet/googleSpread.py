import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 쓸 서비스 API 권한 얻기 []인 이유는 여러 권한을 얻을 수 있기 위함
scope = ["https://spreadsheets.google.com/feeds"]
# 내 계정의 키, 사용할 API 
credentials = ServiceAccountCredentials.from_json_keyfile_name("cred.json",scope)

# 인증 정보를 가지고 인증 시도
gs = gspread.authorize(credentials)

# 스프레드시트 주소
doc = gs.open_by_url("https://docs.google.com/spreadsheets/d/1tuzaqujWCsIYNJryptpcFvI02T4LJujKTVF4uycfq0c/edit#gid=0")
# 첫번째 워크시트
ws = doc.get_worksheet(0)

# 하나의 셀 생성
val = ws.acell("B1").value
print(val)

# 행값 추출
val2 = ws.row_values("1")
print(val2)

# 열값 추출 숫자로 표시
val3 = ws.col_values("1")
print(val3)

# 범위 클래스의 형태로 값을 표시
val4 = ws.range("A1:B3")
print(val4)
for i in val4:
    print(i.value)

# # 하나의 셀
# ws.update_acell("A1","체인지")

# 행 추가 update와 함께 사용 불가
ws.append_row(["sadf","고구마","응응?"]) 