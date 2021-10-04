import os

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


def handle_message(update, context):
    update_txt = f"{update}"
    file_id_init = update_txt.rfind("'file_id':")
    file_id = update_txt[file_id_init:]
    file_id = file_id.split(",")
    file_id = file_id[0]
    print(file_id)
    user_id = update.message.chat_id

    user_language = update.effective_user['language_code']
    if user_language == 'es':
        mensaje = f"Aqui tienes el file_id " \
                  f"\n\n<b>{file_id}</b>" \
                  f"\n\nY por las dudas el metodo update completo:" \
                  f"\n\n<i>{update_txt}</i>"

    else:
        mensaje = f"Here is the file_id" \
                  f"\n\n<b>{file_id}</b>" \
                  f"\n\nAnd just in case, there is the complete update method:" \
                  f"\n\n<i>{update_txt}"
    context.bot.sendMessage(
        chat_id=user_id,
        parse_mode="html",
        text=mensaje
    )


def handle_start(update, context):
    user_first_name = update.effective_user['first_name']

    user_language = update.effective_user['language_code']
    if user_language == 'es':
        mensaje = (f'Hola {user_first_name}! para usarme, solo tienes que enviarme un sticker y yo te voy a devolver '
              'el <i>file_id</i> para que puedas usar ese sticker en tu bot.'
              '\nTambién voy a devolverte el update completo <b>por las dudas</b>')
    else:
        mensaje = (f"Hi {user_first_name}! To use me, you just have to send me a sticker and I will return the "
                   f"<i> file_id </i> so you can use that sticker in your bot."
                   f"\nI'll also give you the full update <b> just in case </b>")

    update.message.reply_text(
        text=mensaje,
        parse_mode="html"
    )


def handle_donaciones(update, context):
    user_first_name = update.effective_user['first_name']

    user_language = update.effective_user['language_code']
    if user_language == 'es':
        mensaje = (f"Si el bot te fue de utilidad y te ahorro tiempo, considera hacer una donación al desarrollador."
                   f"\nPuedes hacerlo desde ko-fi (botón aquí abajo)"
                   f"\nó enviar un mail: stickers-id-dev@telegmail.com")
        button = f"Comprale un Ko-Fi ☕"
    else:
        mensaje = (f"If the bot was useful and saved you time, consider making a donation to the developer."
                   f"\nYou can do it from ko-fi (button below)"
                   f"\nor contact him by mail: stickers-id-dev@telegmail.com")
        button = f"Buy a Ko-Fi ☕"

    update.message.reply_text(
        text= mensaje,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text=button, url='https://ko-fi.com/lucasdeveloper')],
        ])
    )


if __name__ == '__main__':
    updater = Updater(token=os.environ['TOKEN'], use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.sticker, handle_message))
    dp.add_handler(
        CommandHandler('start', handle_start)
    )
    dp.add_handler(
        CommandHandler('donaciones', handle_donaciones)
    )
    updater.start_polling()
    print('Bot esta más vivo que vivin')
    updater.idle()