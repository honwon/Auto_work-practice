# email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
# 정규표현식
import re

# gmail smtp 서버 포트
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# 실제 아이디 비밀번호
SMTP_USER = "moheom98@gmail.com"
SMTP_PASSWORD = 'sksmstkdjqdhkd!'

# None 아무것도 없다 attachment에 대한 변수 안받아도 됨
def send_mail(name, addr, subject, contents, attachment=None):
    # 정규표현식 문장의 앞에 [] 안의 문자가 하나 이상(+)하고 @가 무조건 나옴 .는 어느 한 문자\.는 . ^ 문자열 시작 / 문자열 끝 $
    if not re.match("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", addr):
        print("wrong mail")
        return

    # HTML 텍스트 메일을 담고 있는 메일이다
    msg = MIMEMultipart("alternative")
    if attachment:
        # 텍스트 내용만 가지고 있는게 아니라 데이터도 가지고 있다.
        # mixed가 아니면 제목에 파일 클립 표시가 안나타날수도 있음
        msg = MIMEMultipart("mixed")

    # 보내는 사람
    msg["From"] = SMTP_USER
    # 받을 이메일 주소
    msg["To"] = addr
    # 제목
    msg["Subject"] = name + "님, " + subject

    # 내용은 단순히 넣을 수 없다. 텍스트 메일을 보낸다고 해도 텍스트만 있는게 아니라 이미지도 있을 수 있기 때문에
    # text는 MIMEText 클래스로 만든다. utf-8은 문자를 인식하는 방식
    text = MIMEText(contents, _charset="utf-8")
    
    #내용을 넣을 떈 attach를 사용해야 한다.
    msg.attach(text)

    # 첨부파일이 있으면
    if attachment:
        # 첨부 파일을 가지고 올때 필요한 클래스 첨부파일이기 때문에 TEXT 대신 BASE
        from email.mime.base import MIMEBase
        from email import encoders

        # 내가 지금 넣을 파일의 종류 설정 밑의 두개는 일반 파일
        file_data = MIMEBase("application","octect-stream")
        # 파일 오픈 rb = 컴퓨터가 이해하는 코드로 열겠다 
        file_data.set_payload(open(attachment,"rb").read())
        # SMTP 규정?에 의해 첨부파일은 base64로 변환되어야 한다
        encoders.encode_base64(file_data)

        # 파일명 추출        
        import os
        filename = os.path.basename(attachment)
        # 헤더는 메타데이터 (키, 첨부파일)
        file_data.add_header('Content-Disposition', 'attachment; filename="'+ filename +'"')
        msg.attach(file_data)


    # SSL = 보안 기술
    smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
    # 로그인
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    # 메일 보내기 메세지 문자열로 변경
    smtp.sendmail(SMTP_USER, addr, msg.as_string())
    # 로그아웃
    smtp.close()

#콘텐츠 내용
contents = """안녕하세요
자동화로 보내지는 메일입니다."""

# send_mail 함수 호출
send_mail("김태우", "moheom98@gmail.com", "자동화 메일입니다.", contents,"text.txt")