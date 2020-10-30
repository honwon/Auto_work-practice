from tokenInfo import ID, TOKEN
import telepot
import os
import datetime

def write_log(msg):
    base_dir=os.path.dirname(os.path.realpath(__file__))
    
    f = open(os.path.join(base_dir,'auto.log'),'a')
    f.write('[%s] %s\n' %(str(datetime.datetime.now())[:19],msg))
    f.close

write_log("실행완료")
# 폴더 경로를 구함(파일의 절대 경로를 구함(__file__ = 실행되는 파일에 대한 절대경로))
base_dir=os.path.dirname(os.path.realpath(__file__))

# 각 운영체제에 맞게 경로와 경로 사이를 붙여나감
f = open(os.path.join(base_dir,'msg.txt'),'r',encoding='UTF-8')

a= f.readlines()
write_log('txt파일 읽음')
msg =''
for i in a:
    msg += i.strip() +'\n'

sendInfo= msg.strip()
write_log('msg 조합 완료')
bot= telepot.Bot(TOKEN)
bot.sendMessage(ID,sendInfo)