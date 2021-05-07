from time import time
from telegram_bot.database import errors_db as db

class errors():
    def error(error_id, data):
        db.error(error_id, data, round(time()))
        return True
