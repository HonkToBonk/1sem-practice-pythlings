# core structure of the bot
import telebot
from telebot import types
from mongoengine import *

bot = telebot.TeleBot('1002991204:AAHnJ2q9kV1htX5iRREZpW0Vg_6xOFOOSao')
connect("cinebot_database")


class State(Document):
    user_id = StringField(required=True, unique=True)
    state = ListField()

@bot.message_handler(commands=['help'])
def help_msg(msg):
    bot.send_message(msg.from_user.id, 'Ты можешь подобрать фильм по параметрам или довериться мне и выбрать '
                                           'случайный фильм из тех, что мне известны. Напиши /start и начнем искать!')

@bot.message_handler(commands=['start', 'restart'])
def welcome_msg(msg):
    try:
        user = State(user_id=str(msg.from_user.id))
        user.save()
    except: pass
    type_reply = types.ReplyKeyboardMarkup(one_time_keyboard = True)
    movie = types.KeyboardButton(text="🎬 Фильм")
    series = types.KeyboardButton(text="📺 Сериал")
    type_reply.row(movie, series)
    bot.send_message(msg.chat.id, text="Что хочешь посмотреть, {}?".format(msg.chat.first_name),
                     reply_markup=type_reply)
    State.objects(user_id=str(msg.from_user.id)).update(state='мод')


@bot.message_handler(func = lambda msg: (State.objects(user_id = str(msg.chat.id)))[0].state == 'мод')
def mainmenu(msg):
    popular = types.KeyboardButton("Популярное🍿")
    random = types.KeyboardButton("Случайный фильм🎲")
    actor = types.KeyboardButton("Актер💃🏻")
    director = types.KeyboardButton("Режиссер📽")
    genre = types.KeyboardButton("Жанр🎬")
    name = types.KeyboardButton("Имя фильма🎙")
    year = types.KeyboardButton("Год выпуска 📅 ")
    search_reply = types.ReplyKeyboardMarkup(one_time_keyboard = True)
    search_reply.row(actor, director, genre)
    search_reply.row(year, random)
    search_reply.row(popular, name)
    bot.send_message(msg.chat.id, text="Выбирай критерий👇", reply_markup=search_reply)
    State.objects(user_id=str(msg.from_user.id)).update(state='меню')



@bot.message_handler(func = lambda msg: (State.objects(user_id = str(msg.chat.id)))[0].state == 'меню')
def find_movie(msg):
    if msg.text == "Популярное🍿" or msg.text.lower() == 'популярное':
        State.objects(user_id=str(msg.from_user.id)).update(state='популярное')
    elif msg.text == "Случайный фильм🎲" or msg.text.lower() == 'случайный фильм':
        State.objects(user_id=str(msg.from_user.id)).update(state='случайный фильм')
    elif msg.text == "Актер💃🏻" or msg.text.lower() == 'актер':
        State.objects(user_id=str(msg.from_user.id)).update(state='актер')
    elif msg.text == "Режиссер📽" or msg.text.lower() == 'режиссер':
        State.objects(user_id=str(msg.from_user.id)).update(state='режиссер')
    elif msg.text == "Жанр🎬" or msg.text.lower() == 'жанр':
        State.objects(user_id=str(msg.from_user.id)).update(state='жанр')
    elif msg.text == "Имя фильма🎙" or msg.text.lower() == 'имя фильма':
        State.objects(user_id=str(msg.from_user.id)).update(state='имя фильма')
    elif msg.text == "Год выпуска 📅":
        State.objects(user_id=str(msg.from_user.id)).update(state='год выпуска')
    else:
        bot.send_message(msg.chat.id, text="Я тебя не понимаю")


@bot.message_handler(func = lambda msg: State.objects(user_id = str(msg.chat.id)).first().state == 'популярное')
def search_popular():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = str(msg.chat.id)).first().state == 'случайный фильм')
def search_random():
    pass
@bot.message_handler(func = lambda msg: State.objects(uuser_id = str(msg.chat.id)).first().state == 'актер')
def search_actor():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = str(msg.chat.id)).first().state == 'режиссер')
def search_director():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = str(msg.chat.id)).first().state == 'жанр')
def search_jenre():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = str(msg.chat.id)).first().state == 'имя фильма')
def search_name():
    pass
@bot.message_handler(func = lambda msg: State.objects(uuser_id = str(msg.chat.id)).first().state == 'год выпуска')
def search_year():
    pass


bot.polling()
