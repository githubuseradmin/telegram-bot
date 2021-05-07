from telegram_bot.database import statistics_db as db

class statistics():
    def update_messages():
        return db.update_messages()
    def update_commands():
        return db.update_commands()
    def update_callback_query():
        return db.update_callback_query()
