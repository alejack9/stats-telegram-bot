import logging
import os
from data_layer import save, get
from importlib import import_module
from telegram.ext import CommandHandler
from consts import ADMIN_ID, COMMANDS_DIR

if (ADMIN_ID != -1):
    save(ADMIN_ID, 'admin')

def load(dispatcher):
    for file in os.listdir(os.fsencode(COMMANDS_DIR)):
        filename = os.fsdecode(file)
        if filename.endswith(".py"):
            module_name = f"{os.path.basename(os.path.normpath(COMMANDS_DIR))}.{os.path.splitext(filename)[0]}"
            handler = import_module(module_name)
            logging.info(f"New command found: /{handler.command}")
            dispatcher.add_handler(CommandHandler(handler.command, handler.handle))
