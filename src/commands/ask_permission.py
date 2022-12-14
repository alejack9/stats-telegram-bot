import logging
from telegram import Update
from telegram.ext import CallbackContext
from consts import ADMIN_ID

command = 'ask'

def handle(update: Update, context: CallbackContext):
    info = f"🪪 Id: {update.effective_user.id}\n"
    info += f"First Name: {update.effective_user.first_name}\n"
    info += f"Last Name: {update.effective_user.last_name}\n"
    info += f"User Name: {update.effective_user.username}\n\n"

    context.bot.send_message(chat_id=ADMIN_ID, text=info)
    context.bot.send_message(chat_id=ADMIN_ID, text=f"Send `/allow {update.effective_user.id}` to allow\.", parse_mode='MarkdownV2')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Done.")
