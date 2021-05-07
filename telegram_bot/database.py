import mysql.connector
from contextlib import contextmanager

@contextmanager
def connect():
    try:
        connection = mysql.connector.connect(host = connect.host,
        user = connect.user,
        password = connect.password,
        database = connect.database,
        autocommit = True)
        cursor = connection.cursor()
        yield cursor
    finally:
        connection.close()

class connect_db():
    host = None
    user = None
    password = None
    database = None
    def __init__(self, host, user, password, database):
        try:
            mysql.connector.connect(host = host, user = user, password = password, database = database,
            autocommit = True)
        except mysql.connector.Error as error:
            print("Don't connected")
        connect.host = host
        connect.user = user
        connect.password = password
        connect.database = database

class users_db():
    def add_user(id_telegram):
        with connect() as db:
            db.execute("INSERT INTO `users` (`id_telegram`) VALUES (%s)", (id_telegram,))
            return db.lastrowid
    def check_user(id_telegram):
        with connect() as db:
            db.execute("SELECT * FROM `users` WHERE `id_telegram` = %s", (id_telegram,))
            return bool(len(db.fetchall()))
    def get_user_id(id_telegram):
        with connect() as db:
            db.execute("SELECT id FROM `users` WHERE `id_telegram` = %s LIMIT 1", (id_telegram,))
            result = db.fetchone()
            if result is None:
                return False
            return result[0]
    def user(id_telegram):
        with connect() as db:
            db.execute("SELECT id, id_telegram, reg_time, status, " + \
            "block, actions FROM `users` WHERE `id_telegram` = %s LIMIT 1", (id_telegram,))
            result = db.fetchone()
            if result is None:
                return False
            user = {}
            user["id"] = result[0]
            user["id_telegram"] = result[1]
            user["reg_time"] = result[2]
            user["status"] = result[3]
            user["block"] = result[4]
            user["actions"] = result[5]
            return user
    def actions_update(id_telegram):
        with connect() as db:
            user = users_db.user(id_telegram)
            messages_send = user["actions"] + 1
            db.execute("UPDATE `users` SET `actions` = %s WHERE `id_telegram` = %s", (messages_send, id_telegram))
            return True
    def delete(id_telegram):
        with connect() as db:
            db.execute("DELETE FROM `users` WHERE `id_telegram` = %s", (id_telegram,))
            return True
    def check_action(id_telegram):
        with connect() as db:
            db.execute("SELECT action FROM `users` WHERE `id_telegram` = %s LIMIT 1", (id_telegram,))
            result = db.fetchone()
            if result is None:
                return False
            return result[0]
    def remove_action(id_telegram):
        with connect() as db:
            db.execute("UPDATE `users` SET `action` = 'None' WHERE `id_telegram` = %s", (id_telegram,))
            return True
    def change_action(id_telegram, action):
        with connect() as db:
            db.execute("UPDATE `users` SET `action` = %s WHERE `id_telegram` = %s", (action, id_telegram))
            return True

class commands_db():
    def check_command(command):
        with connect() as db:
            db.execute("SELECT status FROM `commands` WHERE command = %s", (command,))
            result = db.fetchone()
            if result is None:
                return False
            if result[0] == 0:
                return "off"
            return True

class settings_db():
    def check_status():
        with connect() as db:
            db.execute("SELECT value FROM `settings` WHERE `name` = 'status'")
            result = db.fetchone()
            if result is None:
                return False
            if int(result[0]) == 0:
                return False
            return True

    def get_name():
        with connect() as db:
            db.execute("SELECT * FROM `settings` WHERE `name` = 'name'")
            result = db.fetchone()
            if result is None:
                return False
            return result[1]

class errors_db():
    def error(error_id, data, time):
        with connect() as db:
            result = db.execute("INSET INTO (`error_id`, `data`, `time`) VALUES (%s, %s, %s)", (error_id, data, time))
            return result.lastrowid

class callback_query_db():
    def check_callback_query(callback_query):
        with connect() as db:
            db.execute("SELECT status FROM `callback_query` WHERE callback_query = %s", (callback_query,))
            result = db.fetchone()
            if result is None:
                return False
            if result[0] == 0:
                return "off"
            return True

class report_db():
    def send(user_id, text, time):
        with connect() as db:
            db.execute("INSERT INTO `reports` (`user_id`, `text`, `time`) VALUES (%s, %s, %s)", (user_id, text, time))
            return db.lastrowid
    def create_text(user_id, text):
        with connect() as db:
            db.execute("INSERT INTO `reports_text` (`user_id`, `report_text`) VALUES (%s, %s)", (user_id, text))
            return db.lastrowid
    def get_text(user_id):
        with connect() as db:
            db.execute("SELECT report_text FROM `reports_text` WHERE `user_id` = %s LIMIT 1", (user_id,))
            result = db.fetchone()
            if result is None:
                return False
            return result[0]
    def delete_text(user_id):
        with connect() as db:
            db.execute("DELETE FROM `reports_text` WHERE `user_id` = %s", (user_id,))
            return True
    def check_reports(user_id):
        with connect() as db:
            db.execute("SELECT user_id FROM `reports` WHERE `user_id` = %s", (user_id,))
            result = db.fetchall()
            if result is None:
                return 0
            return len(result)

class statistics_db():
    def update_messages():
        with connect() as db:
            db.execute("SELECT messages FROM `statistics` LIMIT 1")
            result = db.fetchone()
            if result is None:
                return False
            messages = result[0] + 1
            db.execute("UPDATE `statistics` SET messages = %s", (messages,))
            return True
    def update_commands():
        with connect() as db:
            db.execute("SELECT commands FROM `statistics` LIMIT 1")
            result = db.fetchone()
            if result is None:
                return False
            commands = result[0] + 1
            db.execute("UPDATE `statistics` SET commands = %s", (commands,))
            return True
    def update_callback_query():
        with connect() as db:
            db.execute("SELECT callback_query FROM `statistics` LIMIT 1")
            result = db.fetchone()
            if result is None:
                return False
            callback_query = result[0] + 1
            db.execute("UPDATE `statistics` SET callback_query = %s", (callback_query,))
            return True

class text_db():

    def text(id, lang):
        with connect() as db:
            db.execute("SELECT `%s` FROM `text` WHERE id = %s LIMIT 1", (lang, id))
            result = db.fetchone()
            if result is None:
                return False
            return result[0]
