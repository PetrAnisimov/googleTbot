import gspread
import telebot


bot_token = "968392706:AAFTwd6cS4H8Nyg3agr24V5OrqrZZBluuBY"
googlesheets_id = "1JLXI4Bt-I7BvPzKFtJq6PXIZSiMVxjKk536iQ4W8pu4"
bot = telebot.TeleBot(bot_token)
gc = gspread.service_account()