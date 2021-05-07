from time import time
from telegram_bot.sql import errors_db

db = errors_db("db/errors.db")

class errors():
    def error(self, error_id, data):
        db.error(error_id, data, round(time()))
        return True
