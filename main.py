import os
from datetime import datetime
import telebot
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env"))
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
print("Running......")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Welcome,Type something to get started mate!')


@bot.message_handler(commands=['help'])
@bot.message_handler(regexp=r'help')
def aid(message):
    bot.send_message(message.chat.id, "Contact @n3tspl0it he is my maker!")


@bot.message_handler(func=lambda m: True)
def greetings(message):
    if message.text.lower() in ['hi', 'hey', 'hello', 'sema', 'vipi', 'niaje', 'holla']:
        bot.send_message(message.chat.id, "Hey there, my name is Chelsea.\n""How can I be of service :).")
    elif message.text.lower() in ['date', 'time', 'day', 'hour']:
        bot.reply_to(message, datetime.now())
    else:
        bot.send_message(message.chat.id, "Love You!!!!!!. \nContact @n3tspl0it , my maker, maybe he "
                                          "can!")


@bot.message_handler(content_types=['document', 'audio'])
def document(message):
    bot.reply_to(message, 'got it')


bot.polling()
