from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def hello(bot, update):
    update.message.reply_text(
        'hello, {}'.format(update.message.from_user.first_name))

def agenda(bot, update):
    update.message.reply_text('https://www.google.com')

def interpreter(bot, update):
    update.message.reply_text('https://www.google.com')

def hackmd(bot, update):
    update.message.reply_text('https://www.google.com')

def icecream(bot, update):
    update.message.reply_text('https://www.google.com')

def information(bot,update):
    reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton('Events', url = 'https://www.google.com'),
        InlineKeyboardButton('map', url = 'https://www.google.com'),
        InlineKeyboardButton('stand', url = 'https://www.google.com')
        ]])
    update.message.reply_text('Agenda' , reply_markup=reply_markup)


updater = Updater('1155065032:AAFPXAyil_mkJCme3aZIRJHlazqQznBgirw')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('agenda', agenda))
updater.dispatcher.add_handler(CommandHandler('interpreter', interpreter))
updater.dispatcher.add_handler(CommandHandler('hackmd', hackmd))
updater.dispatcher.add_handler(CommandHandler('icecream', icecream))
updater.dispatcher.add_handler(CommandHandler('information', information))

updater.start_polling()
updater.idle()
