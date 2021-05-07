from telegram_bot import bot, users, settings, report, statistics
from telegram_bot.database import commands_db as db

class commands():

    def command(result):

        chat_id = result['chat_id']
        text = result['text']
        message_id = result['message_id']

        params = text.split()
        command = params[0]

        check = db.check_command(command)
        if check is False:
            bot.sendMessage(chat_id, "Команды не существует.")
            return False
        if check == "off":
            bot.sendMessage(chat_id, "Команда была отключена. Попробуйте в другой раз.")
            return False

        statistics.update_commands()

        if command == "/start":
            if commands.start(chat_id):
                return True

        if command == "/test":
            if commands.test(chat_id):
                return True

        if command == "/report":
            if report.check_reports(chat_id):
                if report.send(chat_id, text[len("/report "):]):
                    return True
            else:
                keyboard = bot.InlineKeyboard([[["В меню <--", "menu"]]])
                bot.sendMessage(id = chat_id, text = "Вы уже отправили много сообщений. Ожидайте ответа от администрации.", reply_markup = keyboard)
                return True

        if command == "/profile":
            users.profile(chat_id)
            return True

        if command == "/menu":
            keyboard = bot.InlineKeyboard([[["Профиль", "profile"], ["Управление аккаунтом", "settings"]], \
            [["Команды и функции бота", "commands"], ["Написать нам", "report"]]])
            bot.sendMessage(id = chat_id, text = "Выберите одно из действий ниже", reply_markup = keyboard)

        return False

    def start(chat_id):
        keyboard = bot.InlineKeyboard([[["Профиль", "profile"], ["Управление аккаунтом", "settings"]], \
        [["Команды и функции бота", "commands"], ["Написать нам", "report"]]])
        bot.sendMessage(id = chat_id, text = "Привет, я " + settings.get_name() + "\n\n" + \
        "Благодаря мне, ты можешь поиграть в игры в мессенджере Telegram (в том числе с друзьями) 🎲" + \
        "\n\nЧтобы узнать все мои функции - нажми на кнопку снизу." + \
        "\n\nТы также можешь пополнить список функций, если отпишешь нам 🛠" + \
        "\n\nВсе сделано просто для твоего удобства, но если есть какие-то трудности, проблемы, возможно ошибки, " + \
        "то ты можешь написать нам." + \
        "\n\nДля удобства работы, мы храним некоторую информацию от твоих действиях в боте " + \
        "(ответственность за эту информацию не несем)" + \
        "\n\nМы продолжаем разрабатывать бота и дополнять его различными функциями. 🛠" + \
        "\n\nУдачи!", reply_markup = keyboard)
        if users.check_user(chat_id) is False:
            users.add_user(chat_id)
        return True

    def test(chat_id):
        bot.sendMessage(id = chat_id, text = "TEST")
        return True
