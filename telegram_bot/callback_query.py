from telegram_bot import users, settings, report, statistics
from telegram_bot.database import callback_query_db as db

class callback_query():

    def callback_query(result):

        chat_id = result['chat_id']
        data = result['data']
        message_id = result['message_id']

        check = db.check_callback_query(data)

        if check is False:
            #bot.sendMessage(chat_id, "Данной функции не существует.")
            keyboard = bot.InlineKeyboard([[["Профиль", "profile"], ["Управление аккаунтом", "settings"]], \
            [["Команды и функции бота", "commands"], ["Написать нам", "report"]]])
            bot.editMessageText("Данной функции не существует.", id = chat_id, message_id = message_id, reply_markup = keyboard)
            return False
        if check == "off":
            #bot.sendMessage(chat_id, "Функция была отключена. Попробуйте в другой раз.")
            keyboard = bot.InlineKeyboard([[["Профиль", "profile"], ["Управление аккаунтом", "settings"]], \
            [["Команды и функции бота", "commands"], ["Написать нам", "report"]]])
            bot.editMessageText("Функция была отключена. Попробуйте в другой раз.", id = chat_id, message_id = message_id, reply_markup = keyboard)
            return False

        statistics.update_callback_query()

        if data == "profile":
            user = users.get_profile(chat_id)
            status_name = ["пользователем", "Premium пользователем"]
            text_message = "Ваш профиль:\n\n" + \
            "Ваш ID: " + str(user['id']) + "\nДата регистрации: " \
            + str(user['reg_time']) \
            + "\nВы являетесь " + status_name[user['status'] - 1] + "\nКоличество действий: " \
            + str(user['actions'])
            keyboard = bot.InlineKeyboard([[["В меню <--", "menu"]]])
            bot.editMessageText(text_message, id = chat_id, message_id = message_id, reply_markup = keyboard)
            return True

        if data == "menu":
            keyboard = bot.InlineKeyboard([[["Профиль", "profile"], ["Управление аккаунтом", "settings"]], \
            [["Команды и функции бота", "commands"], ["Написать нам", "report"]]])
            bot.editMessageText("Выберите одно из действий", id = chat_id, message_id = message_id, reply_markup = keyboard)
            return True

        if data == "settings":
            keyboard = bot.InlineKeyboard([[["Профиль", "profile"], ["Удалить аккаунт", "confirm_delete_account"]], \
            [["В меню <--", "menu"]]])
            bot.editMessageText("Выберите одно из действий", id = chat_id, message_id = message_id, reply_markup = keyboard)
            return True

        if data == "confirm_delete_account":
            keyboard = bot.InlineKeyboard([[["Да", "delete_account"], ["Нет", "menu"]]])
            bot.editMessageText("Подтверждение удаление аккаунта\n\n" + \
            "При удалении аккаунта, вся информаци, которая у нас имеется о ваших действия в боте, " + \
            "будет удалена.\n\nВы действительно хотите удалить аккаунт ?", id = chat_id, message_id = message_id, reply_markup = keyboard)
            return True

        if data == "delete_account":
            user = users.get_profile(chat_id)
            status_name = ["Пользователь", "Premium пользователь"]
            text_message = "ID пользователя: " + str(user['id']) + "\nДата регистрации: " \
            + str(user['reg_time']) + "\n" \
            + status_name[user['status'] - 1] + "\nКоличество действий: " \
            + str(user['actions']) + \
            "\n\nАккаунт был удален.\n\nЕсли вы напишите боту, то будет создан новый аккаунт."
            if users.delete(chat_id):
                bot.editMessageText(text_message, id = chat_id, message_id = message_id)
                return True
            return False

        if data == "report":
            report.delete_text(chat_id)
            if report.check_reports(chat_id):
                keyboard = bot.InlineKeyboard([[["Отмена | В меню <--", "menu"]]])
                bot.editMessageText("Отправка сообщении администрации\n\n" + \
                "Напишите сообщение", id = chat_id, message_id = message_id, reply_markup = keyboard)
                users.change_action(chat_id, "report")
                return True
            else:
                keyboard = bot.InlineKeyboard([[["В меню <--", "menu"]]])
                bot.editMessageText("Отправка сообщении администрации\n\n" + \
                "Вы уже отправили много сообщений. Ожидайте ответа от администрации.", id = chat_id, message_id = message_id, reply_markup = keyboard)
                return True

        if data == "report_send":
            keyboard = bot.InlineKeyboard([[["В меню <--", "menu"]]])
            bot.editMessageText("Сообщение администрации", id = chat_id, message_id = message_id, reply_markup = keyboard)
            text = report.get_text(chat_id)
            if not text:
                return True
            report.send(chat_id, text)
            report.delete_text(chat_id)
            return True