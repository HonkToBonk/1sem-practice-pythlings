# core structure of the bot
import telebot
from telebot import types
from mongoengine import *

bot = telebot.TeleBot("1159623184:AAEenoQ71Hr4oWUfqvpnbcZRtLq1tDhVR3w")


@bot.message_handler(commands=['start', 'help'])
def welcome_msg(msg):
    if msg.text == '/start':
        go_start_keyboard = types.InlineKeyboardMarkup()
        go_start_btn = types.InlineKeyboardButton(text='Давай начнем', callback_data='go')
        go_start_keyboard.add(go_start_btn)
        bot.send_message(msg.from_user.id, 'Привет!✌🏻\nЯ могу предложить тебе что посмотреть сегодня вечером. Помоги'
                                           'мне выбрать, задав параметры для поиска. Чтобы узнать подробнее - напиши '
                                           '/help, или давай сразу начнем!', reply_markup=go_start_keyboard)

    if msg.text == '/help':
        go_help_keyboard = types.InlineKeyboardMarkup()
        go_help_btn = types.InlineKeyboardButton(text='Понятно, давай начнем', callback_data='go')
        go_help_keyboard.add(go_help_btn)
        bot.send_message(msg.from_user.id, 'Ты можешь: подобрать фильм по параметрам, найти похожий на свой любимый или'
                                           ' довериться мне и выбрать случайный фильм из тех, что мне известны.',
                         reply_markup=go_help_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def type_handling(call):
    type_keyboard = types.ReplyKeyboardMarkup()
    movie = types.KeyboardButton("🎬 Фильм")
    series = types.KeyboardButton("📺 Сериал")
    type_keyboard.row(movie, series)
    if call.data == 'go':
        bot.send_message(call.from_user.id, "Что смотреть будем?", reply_markup=type_keyboard)


bot.polling()
