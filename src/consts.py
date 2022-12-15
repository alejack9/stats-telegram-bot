import logging
import os

class Consts:
    ADMIN_ID = -1

    def set_admin(value):
        if Consts.ADMIN_ID != -1:
            raise Exception('ADMIN_ID already set.')
        Consts.ADMIN_ID = value

    COMMANDS_DIR = 'commands'