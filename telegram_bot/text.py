from telegram_bot.database import text_db as db

class text():

    def text(id, lang = 'en'):
        return db.text(id, lang)
