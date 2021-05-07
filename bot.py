from telegram_bot import bot, users, commands, settings, errors, callback_query, statistics, actions
from telegram_bot.database import connect_db

bot("1124104867:AAHHe3f4Lxs8biGFTwtb16BXeE29rM6x_aU")

connect_db("127.0.0.1", "root", "12345", "test")

update_id = None

while True:
    result = bot.getUpdates(offset = update_id, timeout = 10)
    update_id = result['update_id']
    if result.get("error"):
        errors.error(2, result)

    if result['result']:
        print(result)
        if settings.check_status() is False:
            bot.sendMessage(id = result['chat_id'], text = "На данный момент бот временно отключён. \
            \nПопробуйте написать в другое время.")
        else:
            if users.check_user(result['chat_id']) is False:
                users.add_user(result['chat_id'])
            users.actions_update(result['chat_id'])
            if result['type'] == "callback_query":
                users.remove_action(result['chat_id'])
#                callback_query.callback_query(result['chat_id'], result['data'])
                callback_query.callback_query(result)
#                bot.sendMessage(id = result['chat_id'], text = result['type'])
                bot.answerCallbackQuery(result['id'])
            if result['type'] == "message":
                if result.get("entities") and result['entities'][0]['type'] == "bot_command":
                    users.remove_action(result['chat_id'])
                    commands.command(result)
                else:
                    if result.get("text"):
                        if users.check_action(result['chat_id']):
                            actions.action(result)
                        else:
                            statistics.update_messages()
                            keyboard = bot.InlineKeyboard([[["Профиль", "profile"], ["Управление аккаунтом", "settings"]], \
                            [["Команды и функции бота", "commands"], ["Написать нам", "report"]]])
                            text = "Привет, я не понимаю, что ты хочешь сделать. Выбери ниже."
                            bot.sendMessage(id = result['chat_id'], text = text, reply_markup = keyboard)
                    elif result.get("sticker"):
                        bot.sendSticker(result['chat_id'], result['sticker']['file_id'])
                    else:
                        errors.error(1, result)
