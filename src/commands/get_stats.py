import logging
import psutil
from telegram import Update
from telegram.ext import CallbackContext
from data_layer import get

command = 'stats'

def get_emoji(value):
  if value > 75.0:
    return "🔴"
  elif value > 50.0:
    return "🟠"
  else:
    return "🟢"  

def handle(update: Update, context: CallbackContext):
  if get(update.effective_user.id):
    return context.bot.send_message(chat_id=update.effective_chat.id, text="Not allowed\. Use `/ask` to ask permission\.", parse_mode='MarkdownV2')

  cpu = psutil.cpu_percent(interval=1)
  stats = f"{get_emoji(cpu)} CPU percentage: {cpu} %\n"
  mem = psutil.virtual_memory().percent
  stats += f"{get_emoji(mem)} Memory: {round(mem, 2)} %\n"
  swap = psutil.swap_memory().percent
  stats += f"{get_emoji(swap)} Swap: {round(swap, 2)} %\n"
  disk = psutil.disk_usage('/')
  stats += f"{get_emoji(disk.used / disk.total * 100)} Disk quota (/): {round(disk.used / disk.total * 100, 2)} % "
  
  context.bot.send_message(chat_id=update.effective_chat.id, text=stats)
