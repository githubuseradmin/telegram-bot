import telegram_bot
from telegram_bot.database import commands_db

db = commands_db("db/commands.db")

bot = telegram_bot.Bot()
users = telegram_bot.users()
settings = telegram_bot.settings()
report = telegram_bot.report()
statistics = telegram_bot.statistics()

class commands():

    def command(self, chat_id, text):
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
            if commands.start(self, chat_id):
                return True

        if command == "/test":
            if commands.test(self, chat_id):
                return True

        if command == "/report":
            if report.send(chat_id, text[len("/report "):]):
                return True

        if command == "/profile":
            if users.profile(chat_id):
                return True

        return False

    def start(self, chat_id):
        name = settings.get_name()
        if name:
            keyboard = bot.InlineKeyboard([[["Профиль", "profile"], ["Управление аккаунтом", "settings"]], \
            [["Команды и функции бота", "commands"], ["Написать нам", "report"]]])
            bot.sendMessage(id = chat_id, text = "Привет, я " + settings.get_name() + "\n\n\
Благодаря мне, ты можешь поиграть в игры в мессенджере Telegram (в том числе с друзьями) 🎲, \
получать утром приветствие и информацию о погоде в каком-либо городе, который ты выберешь 🤚 🌤, \
получить ответ на какой-либо пример по математике или по химии 🎒 (на данный момент используются дополнительные сервисы)\
\n\nЧтобы узнать все мои функции на данный момент - нажми на кнопку снизу. \
\n\nТы также можешь пополнить список функций, если отпишешь нам 🛠 \
\n\nВсе сделано просто для твоего удобства, но если есть какие-то трудности, проблемы, возможно ошибки, \
то ты можешь написать нам.\
\n\nМы продолжаем разрабатывать бота и дополнять его различными функциями. 🛠 \
\n\nУдачи!", reply_markup = keyboard)
        if users.check_user(chat_id) is False:
            users.add_user(chat_id)
        return True

    def test(self, chat_id):
        bot.sendMessage(id = chat_id, text = "TEST")
        return True
