import telepot

bot = telepot.Bot('1072189911:AAHz4JM3H6v2lUru8-o6sJ3ru3RKr70oc_s')
id = 1206556142
# bot.sendMessage(id,'안녕하세요')

# 텔레그램 상태표시창 '사진 보내는 중'
bot.sendChatAction(id,'upload_photo')
bot.sendPhoto(id,open('result.png','rb'),caption='프로필사진')
