from telegram_bot import bot, users, settings, report, statistics, errors
#from telegram_bot.database import actions_db as db

class actions():

    def action(result):

        chat_id = result["chat_id"]
        action = users.check_action(chat_id)

        if not action:
            return False

        if action == "report":
            report.create_text(chat_id, result["text"])
            report.confirm(chat_id, result["text"])

        users.remove_action(chat_id)
