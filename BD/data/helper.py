import telebot
from telebot import types

bot = telebot.TeleBot('7020446645:AAH5vqulc9QJGazoUGoWbXeDoBiF_tJPJtc')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! '
                                      f'Это бот помощник, он потсарается решить все ваши проблемы.'
                                      'Если у вас все еще останутся вопросы <u>перейдите в описание бота</u> - там указан'
                                          ' <b>номер</b> по которому вы можете связаться с нами.', parse_mode='html',)
    com(message)

@bot.message_handler(commands=['start'])
def com(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Тех.поддержка', callback_data='edit')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Пополнить баланс', callback_data='edit')
    btn3 = types.InlineKeyboardButton('Вывести средства', callback_data='edit')
    markup.row(btn2, btn3)
    btn4 = types.InlineKeyboardButton('Вернуться назад', url='https://www.kinopoisk.ru/series/749374/')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Доступные команды:', reply_markup=markup)

@bot.message_handler()
def info(message):
    bot.send_message(message.chat.id, f'Пожалуйста, используйте приведенные команды')





bot.polling(none_stop=True)