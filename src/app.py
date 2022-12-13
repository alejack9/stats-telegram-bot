import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from handlers import send_stats, allow_user, ask_permission

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(
    token=os.getenv('TOKEN'), use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('stats', send_stats))
dispatcher.add_handler(CommandHandler('allow', allow_user))
dispatcher.add_handler(CommandHandler('ask', ask_permission))
updater.start_polling()