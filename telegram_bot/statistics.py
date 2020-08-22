from telegram_bot.database import statistics_db

db = statistics_db("db/statistics.db")

class statistics():
    def update_messages(self):
        return db.update_messages()
    def update_commands(self):
        return db.update_commands()
    def update_callback_query(self):
        return db.update_callback_query()
