from Gbot.config import bot, googlesheets_id, gc


@bot.message_handler(commands=['list'])
def list(message):
    bot.send_message(message.chat.id, 'Вот список ваших заказов:')
    sh = gc.open_by_key(googlesheets_id)
    for items in sh.sheet1.col_values(2):
        bot.send_message(message.chat.id, items)