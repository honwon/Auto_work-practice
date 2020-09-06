user_input = input("input: ")
# 쓰기 모드로 열기 txt파일이 없으면 자동으로 생성 기본 내용은 지워진다
datafile = open("textfile.txt", "w")
# user_input의 값을 넣어준 후 앤터
datafile.write(user_input + "\n")
# 프로그램이 종료될 떄 닫기때문에 close 함수 입력 요
datafile.close()