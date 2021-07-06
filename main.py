import os
from telegram.ext import Updater, MessageHandler, Filters


def handle_message(update, context):
    update_txt = f"{update}"
    file_id_init = update_txt.rfind("'file_id':")
    file_id = update_txt[file_id_init:]
    file_id = file_id.split(",")
    file_id = file_id[0]
    print(file_id)
    user_id = update.message.chat_id
    context.bot.sendMessage(
        chat_id=user_id,
        parse_mode= "html",
        text= f"Aqui tienes el file_id \n\n<b>{file_id}</b>\n\nY por las dudas el "
              f"metodo update completo:\n\n<i>{update_txt}</i>"
    )


if __name__ == '__main__':

    updater = Updater(token=os.environ['TOKEN'], use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.sticker, handle_message))
    updater.start_polling()

    print('Bot esta más vivo que vivin')

    updater.idle()