import sqlite3

class users_db():
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def add_user(self, id_telegram, reg_date):
        with self.connection:
            result = self.cursor.execute("INSERT INTO `users` (`id_telegram`, `reg_date`) VALUES (?, ?)", (id_telegram, reg_date))
            return result.lastrowid
    def check_user(self, id_telegram):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `id_telegram` = ?", (id_telegram,)).fetchall()
            return bool(len(result))
    def get_user_id(self, id_telegram):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `id_telegram` = ?", (id_telegram,)).fetchall()
            if len(result) != 1:
                return False
            result = result[0]
            return result[0]
    def user(self, id_telegram):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `id_telegram` = ?", (id_telegram,)).fetchall()
            if len(result) != 1:
                return False
            result = result[0]
            user = {}
            user["id"] = result[0]
            user["id_telegram"] = result[1]
            user["reg_date"] = result[2]
            user["status"] = result[3]
            user["block"] = result[4]
            user["messages_send"] = result[5]
            return user
    def messages_send_update(self, id_telegram):
        with self.connection:
            user = users_db.user(id_telegram)
            messages_send = user["messages_send"] + 1
            self.cursor.execute("UPDATE `users` SET `messages_send` = ? WHERE `id_telegram = ?`", (messages_send, id_telegram))
            return True

class commands_db():
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def check_command(self, command):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `commands` WHERE command = ?", (command,)).fetchall()
            if len(result) != 1:
                return False
            result = result[0]
            if result[1] == 0:
                return "off"
            return True

class settings_db():
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def check_status(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `settings`").fetchall()
            if len(result) != 1:
                return False
            result = result[0]
            if result[0] == 0:
                return False;
            return True
    def get_name(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `settings`").fetchall()
            if len(result) != 1:
                return False
            result = result[0]
            return result[1]

class errors_db():
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def error(self, error_id, data, time):
        with self.connection:
            result = self.cursor.execute("INSET INTO (`error_id`, `data`, `time`) VALUES (?, ?, ?)", (error_id, data, time))
            return result.lastrowid

class callback_query_db():
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def check_callback_query(self, callback_query):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `callback_query` WHERE callback_query = ?", (callback_query,)).fetchall()
            if len(result) != 1:
                return False
            result = result[0]
            if result[1] == 0:
                return "off"
            return True

class report_db():
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def send(self, user_id, text, time):
        with self.connection:
            result = self.cursor.execute("INSERT INTO `reports` (`user_id`, `text`, `time`) VALUES (?, ?, ?)", (user_id, text, time))
            return result.lastrowid

class statistics_db():
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
    def update_messages(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `statistics`").fetchall()
            if len(result) != 1:
                return False
            result = result[0]
            messages = result[0] + 1
            self.cursor.execute("UPDATE `statistics` SET messages = ?", (messages,))
            return True
    def update_commands(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `statistics`").fetchall()
            if len(result) != 1:
                return False
            result = result[0]
            commands = result[1] + 1
            self.cursor.execute("UPDATE `statistics` SET commands = ?", (commands,))
            return True
    def update_callback_query(self):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `statistics`").fetchall()
            if len(result) != 1:
                return False
            result = result[0]
            callback_query = result[2] + 1
            self.cursor.execute("UPDATE `statistics` SET callback_query = ?", (callback_query,))
            return True
