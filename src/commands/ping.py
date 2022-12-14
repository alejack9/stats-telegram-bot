from telegram import Update
from telegram.ext import CallbackContext

command = 'ping'

def handle(update: Update, context: CallbackContext):
  context.bot.send_message(chat_id=update.effective_chat.id, text="pong 🏓")
