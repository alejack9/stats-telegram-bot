import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

import os
from telegram.ext import Updater
import handlers_loader
from consts import Consts

admin = int(os.getenv('ADMIN_ID', '-1'))
if admin == -1:
    logging.warning("No ADMIN_ID found. Send /iamadmin to your bot to set you as admin.")
Consts.set_admin(admin)

updater = Updater(
    token=os.getenv('TOKEN'), use_context=True)

handlers_loader.load(updater.dispatcher)

updater.start_polling()