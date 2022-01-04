import os
import time
from datetime import datetime
from pathlib import Path

import telebot
from dotenv import load_dotenv

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
        bot.send_message(message.chat.id, message.text)
        time.sleep(2)
        bot.send_message(message.chat.id, 'Just kidding!!,I can actually understand you :)')
        time.sleep(2)
        bot.send_message(message.chat.id, "Wait for @n3tspl0it to give me permission to respond to your message.")
        time.sleep(1)
        bot.send_message(message.chat.id, f'Goodbye {message.chat.first_name}, catch you later.')


@bot.message_handler(content_types=['document', 'audio'])
def document(message):
    bot.reply_to(message, 'Got the file,thanks mate')


bot.polling()
