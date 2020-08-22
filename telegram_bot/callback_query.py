import telegram_bot
from telegram_bot.database import callback_query_db

db = callback_query_db("db/callback_query.db")

bot = telegram_bot.Bot()
users = telegram_bot.users()
settings = telegram_bot.settings()
report = telegram_bot.report()
statistics = telegram_bot.statistics()

class callback_query():

    def callback_query(self, chat_id, data):

        check = db.check_callback_query(data)

        if check is False:
            bot.sendMessage(chat_id, "Данной функции не существует.")
            return False
        if check == "off":
            bot.sendMessage(chat_id, "Функция была отключена. Попробуйте в другой раз.")
            return False

        statistics.update_callback_query()

        if data == "profile":
            if users.profile(chat_id):
                return True

    def test(self, chat_id):
        bot.sendMessage(id = chat_id, text = "TEST")
        return True
