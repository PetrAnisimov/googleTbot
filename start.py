from datetime import date
from config import bot,bot_token,googlesheets_id,gc
from dataclasses import dataclass



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Привет, я буду записывать ваши расходы! Введи расходы через дефис в виде [КАТЕГОРИЯ-ЦЕНА]")

@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    try:
        today = date.today().strftime("%d.%m.%y")

        #разделяем сообщения на две части, категория цена
        category, price = message.text.split('-',1)
        text_message = f'На {today} в таблицу расходов добавлена запись: категория {category}, на сумму {price}'
        bot.send_message(message.chat.id, text_message)

        #открываем Google таблицу и добавляем запись
        sh = gc.open_by_key(googlesheets_id)
        sh.sheet1.append_row([today,category,price])
    except:
        # если пользователь ввел неправильную информацию, оповещаем его и просим вводить повторно
        bot.send_message(message.chat.id, "ОШИБКА! Не верный формат данных")


    bot.send_message(message.chat.id, 'Введите расход через дефис в виде [КАТЕГОРИЯ-ЦЕНА]:\nИли выбери другу команду')

