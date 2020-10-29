import requests

AUTH_KEY = '11e175b135f5537063d8eaafb8b1dd243e01b238'

args = {
    'bgn_de': '20191001',
    'end_de': '20191231',
    'sort': 'crp',
    'page_no' : '5'
}

args_st = ''
for k, v in args.items():
    args_st += '&%s=%s' % (k, v)


# get은 뒤에나오는 주소에 접속하겠다.
# ?로 시작하는 부분부터 전달할 데이터 & 표시로 구분이 된다.
res = requests.get(
    'https://opendart.fss.or.kr/api/list.json?crtfc_key=%s%s' % (AUTH_KEY, args_st))

data = res.json()
print(data)
# 만약 에러가 나면
if data['status'] != '000':
    bot.sendMessage(id,'공시정보 조회 실패'+data['message'])
    #에러 메세지 출력
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