from time import time, strftime
from datetime import datetime
from telegram_bot.sql import report_db
from telegram_bot.users import users

db = report_db("db/report.db")
users = users()

class report():
    def __init__(self, bot = None):
        self.bot = bot

    def send(self, chat_id, text):
        if len(text) < 10:
            self.bot.sendMessage(chat_id, "Текст слишком короткий. Текст должен быть от 10 символов.")
            return False
        if len(text) > 100000:
            self.bot.sendMessage(chat_id, "Текст слишком длинный. Текст должен быть до 100 000 символов")
            return False
        user_id = users.get_user_id(chat_id)
        time = round(time())
        result = db.send(user_id, text, time)
        if result:
            self.bot.sendMessage(chat_id, "Вы отправили сообщение администрации.\n\n\
Ваш ID: " + str(user_id) + "\nДата и время: " + datetime.fromtimestamp(time).strftime("%B %d, %Y %H:%M:%S") + "\nТекст: " + text + "\n\nОжидайте ответа.")
            return True
        return False
