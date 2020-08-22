from time import time, strftime
from datetime import datetime
import telegram_bot
from telegram_bot.database import report_db

db = report_db("db/report.db")

bot = telegram_bot.Bot()
users = telegram_bot.users()
settings = telegram_bot.settings()
report = telegram_bot.report()
statistics = telegram_bot.statistics()

class report():

    def send(self, chat_id, text):
        if len(text) < 10:
            bot.sendMessage(chat_id, "Текст слишком короткий. Текст должен быть от 10 символов.")
            return False
        if len(text) > 100000:
            bot.sendMessage(chat_id, "Текст слишком длинный. Текст должен быть до 100 000 символов")
            return False
        user_id = users.get_user_id(chat_id)
        time = round(time())
        result = db.send(user_id, text, time)
        if result:
            bot.sendMessage(chat_id, "Вы отправили сообщение администрации.\n\n\
Ваш ID: " + str(user_id) + "\nДата и время: " + datetime.fromtimestamp(time).strftime("%B %d, %Y %H:%M:%S") + "\nТекст: " + text + "\n\nОжидайте ответа.")
            return True
        return False
