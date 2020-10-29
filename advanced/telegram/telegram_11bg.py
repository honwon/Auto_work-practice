from selenium import webdriver
# 현재시간
import datetime
import os
# csv 파일 읽기
import csv
import telepot

f = open("product.txt", "r")
products = f.readlines()
f.close()

csvFileName = "output.csv"

prices = None
# 파일이 있으면 마지막 가격 정보를 추출함
if os.path.exists(csvFileName):
    f = open(csvFileName, 'r')
    # 가장 마지막의 변수를 꺼내줌 문자열을 가지고 와서 다시 놔누어준다(쉼표기준).
    prices = f.readlines().pop().strip().split(',')
    f.close





driver = webdriver.Chrome('./chromedriver.exe')


try:
    # 변수 지정
    idx = 1
    #가격변동내역 담을 함수
    diff =[]
    #공백으로 시작함
    header = [""]
    #현재시간 입력
    data = [str(datetime.datetime.now())]

    # 반복문을 돌면서 각 주소로 들어감
    for url in products:
        url = url.strip()
        driver.get(url)

        elem = driver.find_element_by_xpath("//h1[@class='title']")
        name = elem.text

        elem = driver.find_element_by_class_name("price_wrap")
        price = elem.find_element_by_class_name("value")
        priceNub = price.text.replace(',','')

        if prices and priceNub != prices[idx]:
           diff.append((name,prices[idx],priceNub))

        idx +=1
        
       # 쉼표를 제거한다
        header.append(name.replace(",", " "))
        data.append(priceNub.replace(",", ""))

    if diff:
        bot = telepot.Bot('1072189911:AAHz4JM3H6v2lUru8-o6sJ3ru3RKr70oc_s')
        msg = ''
        for info in diff:
            #튜플형태이기 떄문에 괄호칠 필요없음
            msg += '- %s\n%s => %s\n' % info
        id = 1206556142
        bot.sendMessage(id,msg)


    # 파일이 존재하지 않는다면
    if not os.path.exists(csvFileName):
        output = open(csvFileName, "a")
        output.write(','.join(header)+'\n')

    output = open(csvFileName, "a")
    output.write(",".join(data)+"\n")

except Exception as e:
    print(e)
finally:
    print('quit')
