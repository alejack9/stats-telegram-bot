import logging
from telegram import Update
from telegram.ext import CallbackContext
from data_layer import set_admin
from consts import Consts

command = 'iamadmin'

def handle(update: Update, context: CallbackContext):
  if Consts.ADMIN_ID != -1:
    logging.info(f"{update.effective_chat.id} requested to become admin but an admin already exists.")
    return

  logging.info(f"{update.effective_chat.id} requested to become admin. Now he's an admin.")
  set_admin(int(update.effective_chat.id))
  context.bot.send_message(chat_id=Consts.ADMIN_ID, text="👑 You are the admin now. 👑")
