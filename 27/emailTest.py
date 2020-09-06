from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = "moheom98@gmail.com"
SMTP_PASSWORD = '2020&"qlsxmadjqtsmstkfa!"'

def send_mail(name, addr, subject, contents):
    # 텍스트 메일을 담고 있는 메일이다
    msg = MIMEMultipart("alternative")

    msg["From"] = SMTP_USER
    msg["To"] = addr
    msg["Subject"] = name + "님, " + subject

    # 내용은 단순히 넣을 수 없다. 텍스트 메일을 보낸다고 해도 텍스트만 있는게 아니라 이미지도 있을 수 있기 때문에
    # text는 MIMEText 클래스로 만든다. utf-8은 문자를 인식하는 방식
    text = MIMEText(contents, _charset="utf-8")
    
    #내용을 넣을 떈 attach를 사용해야 한다.
    msg.attach(text)

    smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
    # 로그인
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    
    # 메일 보내기
    smtp.sendmail(SMTP_USER, addr, msg.as_string())
    
    # 로그아웃
    smtp.close()

contents = """안녕하세요

자동화로 보내지는 메일입니다."""

send_mail("김태우", "moheom98@gmail.com", "자동화 메일입니다.", contents)
