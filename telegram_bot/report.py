from time import time, strftime
from datetime import datetime
from telegram_bot import bot, users, settings, statistics
from telegram_bot.database import report_db as db

class report():

    def send(chat_id, text):
        print(text)
        if len(text) < 10:
            bot.sendMessage(chat_id, "Текст слишком короткий. Текст должен быть от 10 символов.")
            return False
        if len(text) > 100000:
            bot.sendMessage(chat_id, "Текст слишком длинный. Текст должен быть до 100 000 символов")
            return False
        user_id = users.get_user_id(chat_id)
        time_now = round(time())
        result = db.send(user_id, text, time_now)
        if result:
            bot.sendMessage(chat_id, "Вы отправили сообщение администрации.\n\n\
Ваш ID: " + str(user_id) + "\nДата и время: " + datetime.fromtimestamp(time_now).strftime("%B %d, %Y %H:%M:%S") + "\nТекст: " + text + "\n\nОжидайте ответа.")
            return True
        return False

    def confirm(chat_id, text):

        if len(text) < 10:
            keyboard = bot.InlineKeyboard([[["Повторить", "report"]], [["В меню <--", "menu"]]])
            bot.sendMessage(chat_id, "Текст слишком короткий. Текст должен быть от 10 символов.", reply_markup = keyboard)
            return False
        if len(text) > 100000:
            keyboard = bot.InlineKeyboard([[["Повторить", "report"]], [["В меню <--", "menu"]]])
            bot.sendMessage(chat_id, "Текст слишком длинный. Текст должен быть до 100 000 символов", reply_markup = keyboard)
            return False

        keyboard = bot.InlineKeyboard([[["Отправить", "report_send"]], [["Отмена | В меню <--", "menu"]]])
        bot.sendMessage(chat_id, "Отправка сообщении администрации\n\n" + \
        "Ваше сообщение: " + text + \
        "\n\nВы действительно хотите его отправить администрации ?", reply_markup = keyboard)
        return True

    def create_text(chat_id, text):
        user_id = users.get_user_id(chat_id)
        db.create_text(user_id, text)
        return True

    def get_text(chat_id):
        user_id = users.get_user_id(chat_id)
        return db.get_text(user_id)

    def delete_text(chat_id):
        user_id = users.get_user_id(chat_id)
        db.delete_text(user_id)
        return True

    def check_reports(chat_id):
        user_id = users.get_user_id(chat_id)
        reports = db.check_reports(user_id)
        if reports >= 3:
            return False
        return True
