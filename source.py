# core structure of the bot
import telebot
from telebot import types
from mongoengine import *

bot = telebot.TeleBot('1294135442:AAFfLVaYHlzqwTioU_vlWig8TI7M-UT2Tp8')
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
    type_reply = types.InlineKeyboardMarkup()
    movie = types.InlineKeyboardButton(text="🎬 Фильм", callback_data='movie')
    series = types.InlineKeyboardButton(text="📺 Сериал", callback_data='show')
    type_reply.add(movie)
    type_reply.add(series)
    bot.send_message(msg.chat.id, text="Что хочешь посмотреть, {}?".format(msg.chat.first_name),
                     reply_markup=type_reply)
    State.objects(user_id=str(msg.from_user.id)).update(state='меню')


@bot.callback_query_handler(func=lambda call: True)
def mainmenu(call):
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
    bot.send_message(call.from_user.id, text="Выбирай критерий👇", reply_markup=search_reply)


@bot.message_handler(func = lambda msg: State.objects(user_id = msg.from_user.id).first().state == 'меню')
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


@bot.message_handler(func = lambda msg: State.objects(user_id = msg.from_user.id).first().state == 'популярное')
def search_popular():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = msg.from_user.id).first().state == 'случайный фильм')
def search_random():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = msg.from_user.id).first().state == 'актер')
def search_actor():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = msg.from_user.id).first().state == 'режиссер')
def search_director():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = msg.from_user.id).first().state == 'жанр')
def search_jenre():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = msg.from_user.id).first().state == 'имя фильма')
def search_name():
    pass
@bot.message_handler(func = lambda msg: State.objects(user_id = msg.from_user.id).first().state == 'год выпуска')
def search_year():
    pass


bot.polling()
