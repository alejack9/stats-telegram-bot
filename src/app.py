import logging
import os
from telegram.ext import Updater
import handlers_loader

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(
    token=os.getenv('TOKEN'), use_context=True)

handlers_loader.load(updater.dispatcher)

updater.start_polling()