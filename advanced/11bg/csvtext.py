import os

f = open("text.csv","w")
print("파일 생성")

if not os.path.exists("text.csv"):
    print("메롱 메롱")
