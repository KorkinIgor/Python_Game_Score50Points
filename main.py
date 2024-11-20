from random import randint, Random
import telebot
from telebot import types
TOKEN = "7558275337:AAGxJo7gxaZvIsA0wuXhd8r-xXFhDjeyWvc"

bot = telebot.TeleBot(TOKEN)
score = 0
random_cards = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('Кинуть карту')
    bt2 = types.KeyboardButton('Завершить')
    markup.row(bt1)
    markup.row(bt2)
    bot.send_message(message.chat.id, f'Кидай карту {message.from_user.username}!',reply_markup=markup)

@bot.message_handler()
def card(message):
    if message.text == 'Кинуть карту':
        cards_drop = random_cards[randint(1, 20)]
        global score
        score += cards_drop
        bot.send_message(message.chat.id, f'Вам выпала карта: {cards_drop}, у вас {score} очков')
        my_result = score
    if message.text == 'Завершить':
        my_result = score
        bot_result = randint(40, 60)
        if bot_result > 50 and my_result > 50:
            bot.send_message(message.chat.id, f'У вас у обоих больше 50 очков, ничья!')
        elif bot_result > 50 > my_result:
            bot.send_message(message.chat.id, f'У бота больше 50 очков, ты победил!')
        elif bot_result < 50 < my_result:
            bot.send_message(message.chat.id, f'У тебя больше 50 очков, ты проиграл! Очки бота: {bot_result}')
        elif bot_result == my_result == 50:
            bot.send_message(message.chat.id, f'У вас у обоих 50 очков, ничья')
        elif bot_result and my_result <50:
            if my_result > bot_result:
                bot.send_message(message.chat.id, f'У тебя: {my_result} очков, у бота {bot_result} очков, ты победил!')
            elif bot_result > my_result:
                bot.send_message(message.chat.id, f'У тебя: {my_result} очков, у бота {bot_result} очков, ты проиграл!')
            elif bot_result == my_result:
                bot.send_message(message.chat.id, f'У тебя: {my_result} очков, у бота {bot_result} очков, у вас ничья!')
        bot_result = 0
        my_result = 0
        score = 0



bot.polling(non_stop=True)
