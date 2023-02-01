import time
import logging

from telegram import (Update, InlineKeyboardMarkup, InlineKeyboardButton)
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext)

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

# dapatkan token dari botFather dan paste dibawah
TOKEN = 'PASTE DISINI'  # mva_niaga_bot

# Variable untuk membuat menu di telegram setelah user ketik /update
MENU_LAPORAN = {
    'TUNGGAKAN': 1,
    'DAFTAR TUNGGU H-1': 2,
    'Cancel': 'cancel laporan'
    }


def start(update: Update, context: CallbackContext):
    """fungsi ketika user ketik /start"""
    update.message.reply_text(
        text=f'Hai {update.effective_user.first_name} Selamat datang di MVA, saya siap otomasi laporan anda. '
             f'Silahkan ketik /update untuk mengakses laporan yang diinginkan.')


def tunggakan(update: Update, query: Update.callback_query):
    """fungsi saat user memilih menu tunggakan"""
    query.edit_message_text(
        text=f'Laporan tunggakan anda sudah NIHIL')
    query.message.reply_photo(
        photo=open('./img.png', 'rb'),
        caption=f'Saldo Tunggakan sudah di update',
        parse_mode='markdown',
    )


def daftung(update: Update, query: Update.callback_query):
    """fungsi saat user memilih menu daftung"""
    query.edit_message_text(
        text=f'Saldo daftung masih tinggi Boss')


def update_laporan(update: Update, context: CallbackContext):
    """fungsi saat user mengetik /update"""
    menu = MENU_LAPORAN
    update.message.reply_text(
        text=f'Silahkan pilih laporan:',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(key, callback_data=value)] for key, value in menu.items()
                ]))


def menu_query(update: Update, context: CallbackContext) -> None:
    """query untuk input user ke dalam database"""
    query = update.callback_query
    query.answer()
    keyword = query.data

    if keyword == '1':  # TUNGGAKAN
        tunggakan(update, query)
    elif keyword == '2':  # DAFTUNG
        daftung(update, query)
    elif keyword == 'cancel laporan':
        query.message.edit_text('dibatalkan..!')
    else:
        print(keyword)
        query.message.edit_text(text='Tidak ada yang dipilih')


def main() -> None:
    """run the bot"""
    # create the application and pass it your bot's a token
    updater = Updater(TOKEN)

    # add callback query handler for update_laporan function
    updater.dispatcher.add_handler(CallbackQueryHandler(menu_query))

    # add command handler for start function
    start_handler = CommandHandler(command='start', callback=start)
    updater.dispatcher.add_handler(start_handler)

    update_handler = CommandHandler(command='update', callback=update_laporan)
    updater.dispatcher.add_handler(update_handler)

    # Connect to Telegram and wait for messages
    updater.start_polling(timeout=600)

    # Keep the program running until interrupted
    updater.idle()


if __name__ == '__main__':
    main()