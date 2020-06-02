import telegram

bot = telegram.Bot(token='1298674671:AAGl0WlHMts5MaPX-kkQ7FXlUAD3uo9MuZw')

# Check your telegram number
# for i in bot.getUpdates():
#     print(i.message)

bot.send_message(chat_id=1015735757, text= 'hi')