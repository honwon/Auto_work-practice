# tkinter 안의 모든 변수를 들고오겠다.
from tkinter import *

class GUIT():
    def __init__(self):
        # 하나의 창을 만들떄 필요한 클래스 변수
        self.tkhandler = Tk()
        # 크기
        self.tkhandler.geometry('500x500')
        # 제목
        self.tkhandler.title('패스트캠퍼스 자동화 프로그램')

        # 내용, 라벨 클래스 받아옴
        self.label_title = Label(self.tkhandler, text='안녕하세요. 자동화 프로그램입니다.')
        # 한줄씩 쌓는다.
        self.label_title.pack()

        # command 뒤에 버튼을 클릭하면 실행할 함수 지정
        self.btn = Button(self.tkhandler, text='11번가 조회', width=30,command=self.sendMessage)
        self.btn.pack()

        self.label_telegram = Label(self.tkhandler, text ='텔레그램 ID')
        self.label_telegram.pack()
        
        # relief는 디자인
        self.text_telegram = Text(self.tkhandler, width =40, height=1, relief=RIDGE, bd=1)
        self.text_telegram.pack()

        # log테이블 스크롤바와 리스트박스 연동시켜야함
        self.scroll = Scrollbar(self.tkhandler, orient='vertical')
        # 앞의 스크롤바와 같이 움직이게 하는 것 휠로 움직일때 스크롤바와 리스트박스 연동
        self.lbox = Listbox(self.tkhandler, yscrollcommand=self.scroll.set)
        # 스크롤바를 움직일때 뷰를 움직인다
        self.scroll.config(command=self.lbox.yview)

        # 오른쪽 y축 가득 차게
        self.scroll.pack(side='right',fill ='y')

        # 왼쪽, 위아래 양옆 가득 차게, 윈도우 창이 변경되더라도 늘어날 수 있도록
        self.lbox.pack(side='left',fill='both',expand=True)
    

    def sendMessage(self):
        self.append_log("메세지를 전송했습니다.")
        from sendTele import do_auto
        # 텍스트 박스 안의 내용을 들고옴 get다음에 (시작, 끝) 공백 제거를 위해  strip 1.0의 의미는 처음부터
        mssg = self.text_telegram.get('1.0',END).strip()
        print(mssg)
        # 비어있지 않으면
        if mssg :
            do_auto(msg=mssg)
            self.append_log("메세지 전송이 완료됬습니다.")
        else:
            self.append_log("값을 입력해주세용")

    def append_log(self, msg):
        import datetime
        # 시간만 추출함
        now = str(datetime.datetime.now())[11:-7]
        # 마지막에 추가
        self.lbox.insert(END,"[%s] %s" % (now, msg))
        # gui는 변경될때마다 업데이트를 해줘야 한다.
        self.lbox.update()
        # 추가되면서 see함수를 통해 스크롤을 밑으로 내리게함
        self.lbox.see(END)

    #실행하는 함수
    def run(self):
        self.tkhandler.mainloop()


g = GUIT()
g.run()

