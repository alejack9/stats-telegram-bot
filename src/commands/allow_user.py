import logging
from telegram import Update
from telegram.ext import CallbackContext
from data_layer import save
from consts import ADMIN_ID

command = 'allow'

def handle(update: Update, context: CallbackContext):
  if update.effective_user.id != ADMIN_ID:
    return context.bot.send_message(chat_id=update.effective_chat.id, text="Not allowed.")

  if len(context.args) < 1:
    return context.bot.send_message(chat_id=update.effective_chat.id, text="No ID passed.")

  if not context.args[0].isdigit():
    return context.bot.send_message(chat_id=update.effective_chat.id, text="Passed ID is not all digits.")

  save(int(context.args[0]), context.args[1] if len(context.args) > 1 else 'guest')

  context.bot.send_message(chat_id=update.effective_chat.id, text="Allowed.")
