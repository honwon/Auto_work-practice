from tokenInfo import ID, TOKEN
import telepot

# 기본값 아이디 지정
def do_auto(telegram_id=ID,msg="메세지 전송이 완료됬습니다."):

    bot= telepot.Bot(TOKEN)
    bot.sendMessage(telegram_id,msg)