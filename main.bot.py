from transliterate import to_latin, to_cyrillic

import telebot

TOKEN = "8117966844:AAGwU6IDCJEqdMB0WltysOEkV0l9V2TMg1Q"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	javob="Assalom aleykum, Xush kelibsiz!"
# 	javob+="\nMatn kiriting:"
# 	bot.reply_to(message,javob )

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user.first_name  # foydalanuvchining ismi
    javob = f"Assalom aleykum, {user}! Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    javob =lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)

    bot.reply_to(message,javob(msg))





# bot.polling()
bot.infinity_polling()

# matn=input("Matn kiriting:")
#
# if matn.isascii():
#     print(to_cyrillic(matn).title())
# else:print(to_latin(matn))
