import telegram_bot

bot = telegram_bot.Bot("1124104867:AAHHe3f4Lxs8biGFTwtb16BXeE29rM6x_aU")

users = telegram_bot.users()
commands = telegram_bot.commands()
settings = telegram_bot.settings()
errors = telegram_bot.errors()
callback_query = telegram_bot.callback_query()
statistics = telegram_bot.statistics()

update_id = None

while True:
    result = bot.getUpdates(offset = update_id, timeout = 10)
    update_id = result['update_id']
    if result['result']:
        if settings.check_status() is False:
            bot.sendMessage(id = result['chat_id'], text = "На данный момент бот временно отключён. \
            \nПопробуйте написать в другое время.")
        else:
            if result['type'] == "callback_query":
                callback_query.callback_query(result['chat_id'], result['data'])
#                bot.sendMessage(id = result['chat_id'], text = result['type'])
                bot.answerCallbackQuery(result['id'])
            if result['type'] == "message":
                if result.get("entities") and result['entities'][0]['type'] == "bot_command":
                    commands.command(result['chat_id'], result['text'])
                else:
                    if result.get("text"):
                        statistics.update_messages()
                        keyboard = bot.InlineKeyboard([[["Профиль", "profile"], ["Управление аккаунтом", "settings"]], \
                        [["Команды и функции бота", "commands"], ["Помощь", "help"]]])
                        text = "Привет, я не понимаю, что ты хочешь сделать. Выбери ниже."
                        bot.sendMessage(id = result['chat_id'], text = text, reply_markup = keyboard)
                    elif result.get("sticker"):
                        bot.sendSticker(result['chat_id'], result['sticker']['file_id'])
                    else:
                        errors.error(1, result)
