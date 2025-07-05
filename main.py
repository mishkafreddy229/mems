import telebot
from random import choice
from os import listdir
from config import TOKEN

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['монетка'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я бот, который знает разные  мемы и еще бросаю монетки')

@bot.message_handler(commands=['mem'])
def send_mem(message):
    random_mem = choice(listdir('images'))
    with open(f'images/{random_mem}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

bot.infinity_polling()