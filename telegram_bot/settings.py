from telegram_bot.database import settings_db as db

class settings():
    def check_status():
        return db.check_status()
    def get_name():
        return db.get_name()
