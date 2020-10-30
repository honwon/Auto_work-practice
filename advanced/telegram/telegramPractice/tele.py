import requests
import datetime
import telepot



id =1206556142
bot = telepot.Bot("1072189911:AAFniK9CPjIN_fjbLqPt_sUoZXVTaBXq8Ic")


# 오늘날짜 변수
today = datetime.date.today()
# 30일을 뺴준다
startDate = today - datetime.timedelta(days=30) 

print("w중간\n\n\n\n")

args = {
    'bgn_de': startDate.strftime('%Y%m%d'),
    # 시작일과 동일한 포멧팅
    'end_de': today.strftime('%Y%m%d'),
    'sort': 'crp',
    'page_no' : '5'
}

args_st = ''
for k, v in args.items():
    args_st += '&%s=%s' % (k, v)


# get은 뒤에나오는 주소에 접속하겠다.
# ?로 시작하는 부분부터 전달할 데이터 & 표시로 구분이 된다.
res = requests.get(
    'https://opendart.fss.or.kr/api/list.json?crtfc_key=%s%s' % (args_st))

data = res.json()
# 만약 에러가 나면
if data['status'] != '000':
    # 텔레그램 전송
    bot.sendMessage(id,'공시정보 조회 실패'+data['message'])
    # 에러 메세지 출력
    print(data['message'])
else:
    msg=''
    # list 값을 추출
    data_list = data['list']
    for d in data_list:
        # 회사명만 추출
        if not msg=='':
            msg += '\n'
        for k, v in d.items():
            msg += '%s, ' % v
    bot.sendMessage(id,'공시정보 조회 성공\n'+msg)
