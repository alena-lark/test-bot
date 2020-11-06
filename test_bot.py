'''
This is test telegram-bot
'''

# define bot and tasks
import telebot
from telebot import types

token = '<your token here>' # your token
bot = telebot.TeleBot(token)
tasks = []

# start
@bot.message_handler(commands=['start'])
def welcome(message):
    sticker = open('<your sticker name>.webp', 'rb') # your path to sticker
    bot.send_sticker(message.chat.id, sticker)    
    bot.send_message(message.chat.id, 'Hello, my friend!\nThis is your test ToDo List in telegtam.\nLet`s go!')

#main code
@bot.message_handler(content_types=['text'])
def item(message):
    tasks.append(message.text)
    
    #inline keyboard
    markup = types.InlineKeyboardMarkup(row_width=1)
    for task in tasks:
        markup.add(types.InlineKeyboardButton(f'{task}', callback_data=f'{task}'))
    
    bot.send_message(message.chat.id, 'Just do it!', reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        tasks.remove(call.data)
        
        #inline keyboard
        markup = types.InlineKeyboardMarkup(row_width=1)
        for task in tasks:
            markup.add(types.InlineKeyboardButton(f'{task}', callback_data=f'{task}'))

        bot.send_message(call.message.chat.id, 'One task is deleted!\n\nJust do it!', reply_markup=markup)
    
    except (IndexError, ValueError):
        bot.send_message(call.message.chat.id, 'Something is wrong 😅\nTry again, please 😇')

#runing
bot.polling(none_stop=True)















