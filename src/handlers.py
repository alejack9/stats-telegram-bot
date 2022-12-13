import psutil
import os
from telegram import Update
from telegram.ext import CallbackContext
import logging
from data_layer import save, get

admin_id = int(os.getenv('ADMIN_ID'))

save(admin_id, 'admin')

def ask_permission(update: Update, context: CallbackContext):
    info = f"🪪 Id: {update.effective_user.id}\n"
    info += f"First Name: {update.effective_user.first_name}\n"
    info += f"Last Name: {update.effective_user.last_name}\n"
    info += f"User Name: {update.effective_user.username}\n\n"
    info += f"Send `/allow {update.effective_user.id}` to allow\."

    context.bot.send_message(chat_id=admin_id, text=info, parse_mode='MarkdownV2')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Done.")

def get_emoji(value):
  if value > 75.0:
    return "🔴"
  elif value > 50.0:
    return "🟠"
  else:
    return "🟢"  

def send_stats(update: Update, context: CallbackContext):
  if get(update.effective_user.id):
    return context.bot.send_message(chat_id=update.effective_chat.id, text="Not allowed\. Use `/ask` to ask permission\.", parse_mode='MarkdownV2')

  cpu = psutil.cpu_percent()
  stats = f"{get_emoji(cpu)} CPU percentage: {cpu} %\n"
  mem = psutil.virtual_memory()
  stats += f"{get_emoji(mem.used / mem.total * 100)} Memory: {round(mem.used / mem.total * 100, 2)} %\n"
  disk = psutil.disk_usage('/')
  stats += f"{get_emoji(disk.used / disk.total * 100)} Disk quota (/): {round(disk.used / disk.total * 100, 2)} % "
  
  context.bot.send_message(chat_id=update.effective_chat.id, text=stats)

def allow_user(update: Update, context: CallbackContext):
  if update.effective_user.id != admin_id:
    return context.bot.send_message(chat_id=update.effective_chat.id, text="Not allowed.")

  if not context.args[0].isdigit():
    return context.bot.send_message(chat_id=update.effective_chat.id, text="Passed ID is not all digits.")

  save(int(context.args[0]), context.args[1] if len(context.args) > 1 else 'guest')

  context.bot.send_message(chat_id=update.effective_chat.id, text="Allowed.")
