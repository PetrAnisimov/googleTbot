import gspread
import telebot


bot_token = "muda968392706:AAFTwd6cS4H8Nyg3agr24V5OrqrZZBluuBYber"
googlesheets_id = "1JLXI4Bt-I7BvPzKFtJq6PXIZSiMVxjKk536iQ4W8pu4"
bot = telebot.TeleBot(bot_token)
gc = gspread.service_account()
