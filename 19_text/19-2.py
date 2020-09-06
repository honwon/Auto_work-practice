# open은 두개의 값을 받음 경로, 할 행동 text 파이을 ANSI로 등록
datafile = open("data.txt","r")

line = "init"
while line:
    # 한문장씩 받아오기 strip = 양 끝에 존재하는 공백과 \n 삭제
    line = datafile.readline().strip()
    print(line)
