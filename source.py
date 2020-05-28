# core structure of the bot
import telebot
from telebot import types
from mongoengine import *
from os import environ

TOKEN = environ['TOKEN']

bot = telebot.TeleBot(TOKEN)


class State(Document):
    user = StringField(required=True)
    name = BooleanField(default=False)
    type = BooleanField(default=False)
    genre = BooleanField(default=False)
    actor = BooleanField(default=False)
    year = BooleanField(default=False)
    director = BooleanField(default=False)
    popular = BooleanField(default=False)
    random = BooleanField(default=False)


@bot.message_handler(commands=['start'])
def welcome_msg(msg):
    if msg.text == '/start':
        user = State(user=msg.from_user.username, type=False, popular=False, random=False, actor=False, director=False,
                     genre=False, name=False, year=False)
        type_reply = types.InlineKeyboardMarkup()
        movie = types.InlineKeyboardButton(text="🎬 Фильм", callback_data='movie')
        series = types.InlineKeyboardButton(text="📺 Сериал", callback_data='show')
        type_reply.add(movie)
        type_reply.add(series)
        bot.send_message(msg.chat.id, text="Что хочешь посмотреть, {}?".format(msg.from_user.first_name),
                         reply_markup=type_reply)


@bot.message_handler(commands=['help'])
def help_msg(msg):
    if msg.text == '/help':
        bot.send_message(msg.from_user.id, 'Ты можешь подобрать фильм по параметрам или довериться мне и выбрать '
                                           'случайный фильм из тех, что мне известны. Напиши /start и начнем искать!')


@bot.callback_query_handler(func=lambda call: True)
def mainmenu(call):
    if call.data == "movie":
        State.type = True
    popular = types.KeyboardButton("Популярное🍿")
    random = types.KeyboardButton("Случайный фильм🎲")
    actor = types.KeyboardButton("Актер💃🏻")
    director = types.KeyboardButton("Режиссер📽")
    genre = types.KeyboardButton("Жанр🎬")
    name = types.KeyboardButton("Имя фильма🎙")
    year = types.KeyboardButton("Год выпуска 📅 ")
    back = types.KeyboardButton("Назад👆")
    search_reply = types.ReplyKeyboardMarkup()
    search_reply.row(actor, director, genre)
    search_reply.row(year, random)
    search_reply.row(popular, name)
    search_reply.row(back)
    bot.send_message(call.from_user.id, text="Выбирай критерий👇", reply_markup=search_reply)


@bot.message_handler(func=lambda call: True)
def find_movie(msg):
    if msg.text == "Популярное🍿":
        # проверка состояния базы и поиск фильма/сериала соответственно
        markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='url', url="https://vk.com")
        markup.add(url_btn)
        bot.send_message(msg.chat.id, text="DEBUG", reply_markup=markup)
    elif msg.text == "Случайный фильм🎲":
        # проверка состояния базы и поиск фильма/сериала соответственно
        markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='url', url="https://vk.com")
        markup.add(url_btn)
        bot.send_message(msg.chat.id, text="DEBUG", reply_markup=markup)
    elif msg.text == "Актер💃🏻":
        # проверка состояния базы и поиск фильма/сериала соответственно
        markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='url', url="https://vk.com")
        markup.add(url_btn)
        bot.send_message(msg.chat.id, text="DEBUG", reply_markup=markup)
    elif msg.text == "Режиссер📽":
        # проверка состояния базы и поиск фильма/сериала соответственно
        markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='url', url="https://vk.com")
        markup.add(url_btn)
        bot.send_message(msg.chat.id, text="DEBUG", reply_markup=markup)
    elif msg.text == "Жанр🎬":
        # проверка состояния базы и поиск фильма/сериала соответственно
        markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='url', url="https://vk.com")
        markup.add(url_btn)
        bot.send_message(msg.chat.id, text="DEBUG", reply_markup=markup)
    elif msg.text == "Имя фильма🎙":
        # проверка состояния базы и поиск фильма/сериала соответственно
        markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='url', url="https://vk.com")
        markup.add(url_btn)
        bot.send_message(msg.chat.id, text="DEBUG", reply_markup=markup)
    elif msg.text == "Год выпуска 📅":
        # проверка состояния базы и поиск фильма/сериала соответственно
        markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='url', url="https://vk.com")
        markup.add(url_btn)
        bot.send_message(msg.chat.id, text="DEBUG", reply_markup=markup)

    elif msg.text == "Назад👆":
        # обновление состояния базы и переход на уровень назад
        bot.send_message(msg.chat.id, text="DEBUG")

    else:
        bot.send_message(msg.chat.id, text="Я тебя не понимаю")


bot.polling()
