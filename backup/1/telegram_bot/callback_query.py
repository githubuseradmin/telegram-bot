from telegram_bot.sql import callback_query_db
from telegram_bot.users import users
from telegram_bot.settings import settings
from telegram_bot.report import report
from telegram_bot.statistics import statistics

db = callback_query_db("db/callback_query.db")

statistics = statistics()

class callback_query():
    def __init__(self, bot):
        self.bot = bot
        self.settings = settings()
        self.users = users(bot)
        self.report = report(bot)

    def callback_query(self, chat_id, data):

        check = db.check_callback_query(data)

        if check is False:
            self.bot.sendMessage(chat_id, "Данной функции не существует.")
            return False
        if check == "off":
            self.bot.sendMessage(chat_id, "Функция была отключена. Попробуйте в другой раз.")
            return False

        statistics.update_callback_query()

        if data == "profile":
            if self.users.profile(chat_id):
                return True

    def test(self, chat_id):
        self.bot.sendMessage(id = chat_id, text = "TEST")
        return True
