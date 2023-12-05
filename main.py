import telebot
import requests
import json
from telebot import types
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6935118032:AAHBJ3vkhvB_sPIwVyRxD9_dPij0RcZIPAM')
api = 'bc2b8bbe0159f288f514f595ef0feba2'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Узнать погоду', callback_data='weather')
    btn2 = types.InlineKeyboardButton('Посмотреть на капибару', callback_data="capibara")
    markup.row(btn1, btn2)  # Using the add() method to add buttons in a single row
    markup.add()
    bot.send_message(message.chat.id, f'привет, {message.from_user.first_name}, что тебе от меня надо?', reply_markup=markup)

@bot.message_handler(commands=['restart'])
def restart(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Узнать погоду', callback_data='weather')
    btn2 = types.InlineKeyboardButton('Посмотреть на капибару', callback_data="capibara")
    markup.row(btn1, btn2)  # Using the add() method to add buttons in a single row
    markup.add()
    bot.reply_to(message, f'Бот перезапущен. Привет, {message.from_user.first_name}, что тебе от меня надо?', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.InlineKeyboardMarkup()
    btn3 = types.InlineKeyboardButton('Меню', callback_data='menu')
    markup.row(btn3)
    markup.add()
    bot.send_message(message.chat.id, f'{message.from_user.first_name},  я знаю, что у вас сейчас трудная ситуация, и я хочу поддержать вас. Не стоит бояться обращаться за помощью, ведь мы все иногда сталкиваемся с трудностями. Важно помнить, что каждая ситуация временна, и всё обязательно наладится. Если вам нужна помощь или поддержка, не стесняйтесь обратиться к близким людям или специалистам. Помните, что самое главное — это сохранять спокойствие и веру в лучшее.', reply_markup=markup)

@bot.message_handler(commands=['weather'])
def weather(message):
    ask_for_weather(message)

@bot.message_handler(commands=['getpic'])
def weather(message):
    markup = types.InlineKeyboardMarkup()
    btn3 = types.InlineKeyboardButton('Меню', callback_data='menu')
    markup.row(btn3)
    markup.add()
    image = 'capi.png'
    file = open('./' + image, 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)

bot.polling(none_stop=True)