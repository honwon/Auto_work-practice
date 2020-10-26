from selenium import webdriver
# 현재시간
import datetime
import os
# csv 파일 읽기
import csv

f = open("product.txt", "r")
products = f.readlines()

csvFileName="ouput.csv"

driver = webdriver.Chrome('./chromedriver.exe')


try:
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
       priceNub = price.text

       # 쉼표를 제거한다
       header.append(name.replace(",", " "))
       print(header)
       data.append(priceNub.replace(",", ""))
       print(data)

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
