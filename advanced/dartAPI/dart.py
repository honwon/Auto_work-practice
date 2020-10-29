import requests

AUTH_KEY = '11e175b135f5537063d8eaafb8b1dd243e01b238'

bgn_de = '20190101'
end_de = '20191231'


# get은 뒤에나오는 주소에 접속하겠다.
# ?로 시작하는 부분부터 전달할 데이터 & 표시로 구분이 된다.
res = requests.get("https://opendart.fss.or.kr/api/list.json?crtfc_key=%s&bgn_de=%s&end_de=%s" % (AUTH_KEY, bgn_de, end_de))

data = res.json()

print(data)
# list 값을 추출
data_list = data['list']
for d in data_list:
    # 회사명만 추출
    print(d['corp_name'])
