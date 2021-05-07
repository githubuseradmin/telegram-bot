from telegram_bot import bot
# from time import time, strftime
# from datetime import datetime
from telegram_bot.database import users_db as db

class users():
    def add_user(id):
#        if db.add_user(id, round(time())):
        if db.add_user(id):
            return True
        return False
    def check_user(id):
        return db.check_user(id)
    def get_user_id(id):
        return db.get_user_id(id)
    def get_user(id):
        return db.get_user(id)
    def profile(id):
        user = db.user(id)
        if user is False:
            return False
        status_name = ["пользователем", "Premium пользователем"]
        bot.sendMessage(id, "Ваш профиль:\n\n" + \
        "Ваш ID: " + str(user['id']) + "\nДата регистрации: " \
        + str(user['reg_time']) \
        + "\nВы являетесь " + status_name[user['status'] - 1] + "\nКоличество сообщений: " \
        + str(user['actions']))
        return True
    def get_profile(id):
        user = db.user(id)
        if user is False:
            return False
        return user
    def actions_update(id):
        if users.check_user(id):
            return db.actions_update(id)
    def delete(id):
        return db.delete(id)
    def check_action(id):
        action = db.check_action(id)
        if action == "None":
            return False
        return action
    def remove_action(id):
        return db.remove_action(id)
    def change_action(id, action):
        return db.change_action(id, action)
