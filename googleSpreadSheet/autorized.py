import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
doc = gs.create("온라인테스트 2")

# 데이터를 넣는 것과 공유는 순서 상관 없다.
ws = doc.get_worksheet(0)

for i in range(5):
    ws.append_row([i,str(i)+"번 행","외로운 배생활 "+str(i)+"일 차"])

# 이메일 주소가 들어감 사용자 권한 설정 reader-읽기 전용, writer-쓰기 전용 소유자가 내가 아니면 공유 문서에서 확인 가능
doc.share("moheom98@gmail.com",perm_type="user",role="owner")