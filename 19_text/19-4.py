user_input = input("input: ")
# 수정 모드로 열기 txt파일에 추가로 설정
datafile = open("textfile.txt", "a")
# user_input의 값을 넣어준 후 앤터
datafile.write(user_input + "\n")
# 프로그램이 종료될 떄 닫기때문에 close 함수 입력 요
datafile.close()