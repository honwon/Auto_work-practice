# open은 두개의 값을 받음 경로, 할 행동 text 파이을 ANSI로 등록
datafile = open("data.txt","r")
# 모든 내용을 가지고 옴
dataread = datafile.read()
print(dataread)