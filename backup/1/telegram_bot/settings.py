from telegram_bot.sql import settings_db

db = settings_db("db/settings.db")

class settings():
    def check_status(self):
        return db.check_status()
    def get_name(self):
        return db.get_name()
