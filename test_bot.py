# -*- coding: utf-8 -*-


# define bot and tasks
import telebot

token = '<your tiken here>'
bot = telebot.TeleBot(token)
tasks = []

# start
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('cat.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)    
    bot.send_message(message.chat.id, 'Hello, my friend!\nThis is your test ToDo List in telegtam.\nLet`s go!')
    
# main code
@bot.message_handler(content_types=['text'])
def item(message):
    if 'delete' in message.text.strip().lower().split():
        try:
            num = int(message.text.strip().split()[1]) - 1
            tasks.pop(num)
            bot.send_message(message.chat.id, 'Just Do It!\n'+'\n'.join(str(i+1) + ') ' + task for i,task in enumerate(tasks)))
        except (IndexError, ValueError):
            bot.send_message(message.chat.id, 'Something is wrong 😅\nTry again, please 😇')
    else:
        tasks.append(message.text)
        bot.send_message(message.chat.id, 'Just Do It!\n'+'\n'.join(str(i+1) + ') ' + task for i,task in enumerate(tasks)))

#runing
bot.polling(none_stop=True)