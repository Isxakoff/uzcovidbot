# -*- coding: utf-8 -*-

# Copyright (C) 2020 Botir Ziyatov <botirziyatov@gmail.com>
# This program is free software: you can redistribute it and/or modify

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from covid19 import Covid19

buttons = ReplyKeyboardMarkup([['Status'], ['Dunyo']], resize_keyboard=True)
covid = Covid19()

def start(update, context):
    update.message.reply_html(
        '<b>Assalomu Alaykum, {}</b>\n \n Men covid 19 haqida malumot beraman  @codertj'.format(update.message.from_user.first_name), reply_markup=buttons)
    return 1

def stats(update, context):
    data = covid.getByCountryCode('UZ')
    update.message.reply_html(
        '🇺🇿 <b>Uzbekistonda</b>\n \n<b>Kasallangalar:</b> {}\n<b>Tuzalganlar:</b> {}\n<b>Halok Bolganlar:</b> {}'.
            format(
            data['confirmed'],
            data['recovered'],
            data['deaths']), reply_markup=buttons)

def world(update, context):
    data = covid.getLatest()
    update.message.reply_html(
        '🌎 <b>Dunyoda</b>\n \n<b>Kasallangalar:</b> {}\n<b>Tuzalganlar</b> {}\n<b>Halok Bolganlar:</b> {}'.format(
            "{:,}".format(data['confirmed']),
            "{:,}".format(data['recovered']),
            "{:,}".format(data['deaths'])
        ), reply_markup=buttons)

updater = Updater('TOOOOOOOOOOOOKEN', use_context=True)
conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start)],
    states={
        1: [MessageHandler(Filters.regex('^(Status)$'), stats),
            MessageHandler(Filters.regex('^(Dunyo)$'), world),
            ]
    },
    fallbacks=[MessageHandler(Filters.text, start)]
)

updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
