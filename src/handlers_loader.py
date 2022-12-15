import logging
import os
from data_layer import save, get
from importlib import import_module
from telegram.ext import CommandHandler
from consts import Consts

def load(dispatcher):
    for file in os.listdir(os.fsencode(Consts.COMMANDS_DIR)):
        filename = os.fsdecode(file)
        if filename.endswith(".py"):
            module_name = f"{os.path.basename(os.path.normpath(Consts.COMMANDS_DIR))}.{os.path.splitext(filename)[0]}"
            handler = import_module(module_name)
            logging.info(f"New command found: /{handler.command}")
            dispatcher.add_handler(CommandHandler(handler.command, handler.handle))
