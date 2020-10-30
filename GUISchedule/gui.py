# tkinter 안의 모든 변수를 들고오겠다.
from tkinter import *

class GUIT():
    def __init__(self):
        self.tkhandler = Tk()
        # 크기
        self.tkhandler.geometry('500x500')
        # 제목
        self.tkhandler.title('패스트캠퍼스 자동화 프로그램')
        # 내용, 라벨 클래스 받아옴
        self.label_title = Label(self.tkhandler, text='안녕하세요. 자동화 프로그램입니다.')
        # 한줄씩 쌓는다.
        self.label_title.pack()

        self.btn = Button(self.tkhandler, text='11번가 조회', width=30)
        self.btn.pack()

        self.label_telegram = Label(self.tkhandler, text ='텔레그램 ID')
        
        self.text_telegram = Text(self.tkhandler, width =40, height=1, relief=RIDGE, bd=1)
        self.text_telegram.pack()

    #실행하는 함수
    def run(self):
        self.tkhandler.mainloop()

g = GUIT()
g.run()

