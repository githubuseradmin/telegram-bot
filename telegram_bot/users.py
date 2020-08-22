from time import time, strftime
from datetime import datetime
from telegram_bot.database import users_db

db = users_db("db/users.db")

bot = telegram_bot.Bot()

class users():
    def add_user(self, id):
        if db.add_user(id, round(time())):
            return True
        return False
    def check_user(self, id):
        return db.check_user(id)
    def get_user_id(self, id):
        return db.get_user_id(id)
    def get_user(self, id):
        return db.get_user(id)
    def profile(self, id):
        user = db.user(id)
        if user is False:
            return False
        status_name = ["пользователем", "Premium пользователем"]
        bot.sendMessage(id, "Ваш профиль:\n\n\
Ваш ID: " + str(user['id']) + "\nДата регистрации: " \
        + datetime.fromtimestamp(user['reg_date']).strftime("%B %d, %Y %H:%M:%S") \
        + "\nВы являетесь " + status_name[user['status'] - 1] + "\nКоличество сообщений: " \
        + str(user['messages_send']))
        return True
    def messages_send_update(self, id):
        if users.check_user(id):
            return db.messages_send_update(id)
