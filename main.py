from config import bot
import start
from Gbot.config import bot, googlesheets_id, gc



def send_welcome(message):
    return send_welcome(message)

def repeat_all_message(message):
    return repeat_all_message(message)

#список всех  товаров
@bot.message_handler(commands=['list'])
def list(message):
    bot.send_message(message.chat.id, 'Вот список ваших заказов:')
    sh = gc.open_by_key(googlesheets_id)
    for items in sh.sheet1.col_values(2):
        bot.send_message(message.chat.id, items)



if __name__ == '__main__':
    bot.polling(none_stop=True)
