import requests
import json

def main():
    pass

class bot():

    def __init__(self, token = None, url = None):
        if url is None:
            self.url = "https://api.telegram.org/bot"
        else:
            self.url = url

        if token:
            self.request_url = self.url + token

    def getUpdates(self, offset = None, timeout = None):
        """
        getUpdates

        offset (int, None | default: None) - last update_id | offset Telegram API method getUpdates
        timeout (int | default: 0) - timeout | timeout Telegram API method getUpdates

        return

        result (array) ('result' (bool), if an error then return 'error' (int) = error code,
        if result == True return 'update_id' (int) - last update id + 1)

        (True - new message, False - no new message) |
        if result == True - 'update_id' int - last update id + 1, 'id' int = id chat,
        'text' - a text)) - result
        """
        data = {}
        if offset:
            data['offset'] = offset
        if timeout:
            data['timeout'] = timeout
        request = requests.post(f'{self.request_url}/getUpdates', data = data)
        request_json = request.json()
        if request_json['ok'] == False:
            print("Not ok")
            print("[ERROR 1] Telgram API return 'ok': False")
            result = {}
            result["error"] = 1
            result["result"] = False
            return result
        if request_json['result']:
            result = {}
            result['result'] = True
            result['update_id'] = request_json['result'][0]['update_id'] + 1
            if request_json['result'][0].get("message"):
                result['type'] = "message"
                result['message_id'] = request_json['result'][0]['message']['message_id']
                if request_json['result'][0]['message'].get("from"):
                    result['from_id'] = request_json['result'][0]['message']['from']['id']
                    result['from_is_bot'] = request_json['result'][0]['message']['from']['is_bot']
                    result['from_first_name'] = request_json['result'][0]['message']['from']['first_name']
                    result['from_last_name'] = request_json['result'][0]['message']['from']['last_name']
                    result['from_username'] = request_json['result'][0]['message']['from']['username']
                    result['from_language_code'] = request_json['result'][0]['message']['from']['language_code']
                result['chat_id'] = request_json['result'][0]['message']['chat']['id']
                result['chat_first_name'] = request_json['result'][0]['message']['chat']['first_name']
                result['chat_last_name'] = request_json['result'][0]['message']['chat']['last_name']
                result['chat_username'] = request_json['result'][0]['message']['chat']['username']
                result['chat_type'] = request_json['result'][0]['message']['chat']['type']
                result['date'] = request_json['result'][0]['message']['date']
                if request_json['result'][0]['message'].get("text"):
                    result['text'] = request_json['result'][0]['message']['text']
                if request_json['result'][0]['message'].get("sticker"):
                    result['sticker'] = request_json['result'][0]['message']['sticker']
                if request_json['result'][0]['message'].get("entities"):
                    result['entities'] = request_json['result'][0]['message']['entities']
                return result
            elif request_json['result'][0].get("callback_query"):
                result['type'] = "callback_query"
                result['id'] = request_json['result'][0]['callback_query']['id']
                result['from_id'] = request_json['result'][0]['callback_query']['from']['id']
                result['from_is_bot'] = request_json['result'][0]['callback_query']['from']['is_bot']
                result['from_first_name'] = request_json['result'][0]['callback_query']['from']['first_name']
                result['from_last_name'] = request_json['result'][0]['callback_query']['from']['last_name']
                result['from_username'] = request_json['result'][0]['callback_query']['from']['username']
                if request_json['result'][0]['callback_query'].get("message"):
                    result['message_id'] = request_json['result'][0]['callback_query']['message']['message_id']
                    result['message_from_id'] = request_json['result'][0]['callback_query']['message']['from']['id']
                    result['message_from_is_bot'] = request_json['result'][0]['callback_query']['message']['from']['is_bot']
                    result['message_from_first_name'] = request_json['result'][0]['callback_query']['message']['from']['first_name']
                    result['message_from_username'] = request_json['result'][0]['callback_query']['message']['from']['username']
                    result['chat_id'] = request_json['result'][0]['callback_query']['message']['chat']['id']
                    result['chat_first_name'] = request_json['result'][0]['callback_query']['message']['chat']['first_name']
                    result['chat_last_name'] = request_json['result'][0]['callback_query']['message']['chat']['last_name']
                    result['chat_username'] = request_json['result'][0]['callback_query']['message']['chat']['username']
                    result['chat_type'] = request_json['result'][0]['callback_query']['message']['chat']['type']
                    result['date'] = request_json['result'][0]['callback_query']['message']['date']
                    result['text'] = request_json['result'][0]['callback_query']['message']['text']
                    result['inline_keyboard'] = request_json['result'][0]['callback_query']['message']['reply_markup']['inline_keyboard'][0]
                result['chat_instance'] = request_json['result'][0]['callback_query']['chat_instance']
                if request_json['result'][0]['callback_query'].get("data"):
                    result['data'] = request_json['result'][0]['callback_query']['data']
                return result
        else:
            result = {}
            result['result'] = False
            result['update_id'] = offset
            return result
    def sendMessage(self, id, text, reply_markup = None, parse_mode = None, disable_web_page_preview = None, \
    disable_notification = None, reply_to_message_id = None):
        """
        sendMessage

        id (int, Required) - id chat
        text (string, Required) - a text
        reply_markup (array) - keyboard

        Return

        result (bool) - return Telegram API 'ok'
        """
        data = {}
        data['chat_id'] = id
        data['text'] = text
        if reply_markup:
            data['reply_markup'] = json.dumps(reply_markup)
        if parse_mode:
            data['parse_mode'] = parse_mode
        if disable_web_page_preview:
            data['disable_web_page_preview'] = disable_web_page_preview
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        send = requests.post(f'{self.request_url}/sendMessage', data = data)
        send_json = send.json()
        result = send_json['ok']
        return result
    def answerCallbackQuery(self, id, text = None, show_alert = None, url = None, cache_time = None):
        """
        answerCallbackQuery

        id (int, Required) - Unique identifier for this query

        Return

        result (bool) - return Telegram API 'ok'
        """
        data = {}
        data['callback_query_id'] = id
        if text:
            data['text'] = text
        if show_alert:
            data['show_alert'] = show_alert
        if url:
            data['url'] = url
        if cache_time:
            data['cache_time'] = cache_time
        send = requests.post(f'{self.request_url}/answerCallbackQuery', data = data)
        send_json = send.json()
        result = send_json['ok']
        return result
#    def InlineKeyboardMarkup(self, buttons):
#        """
#        InlineKeyboardMarkup
#
#        buttons (array, Required) - buttons array
#
#        Return
#
#        result (dict with array) - dict with array for 'reply_markup' Telegram API 'sendMessage'
#        """
#        result = {'inline_keyboard': [buttons]}
#        return result
#    def InlineKeyboardButton(self, buttons):
#        """
#        InlineKeyboardButton
#
#        buttons (array, Required) - buttons array
#
#        Return
#
#        result (array) - buttons array
#        """
#        result = buttons
#        return result
    def InlineKeyboard(self, buttons):
        """
        InlineKeyboardButton

        buttons (array, Required) - buttons array

        Return

        result (array) - buttons array
        """
        if len(buttons) == 0 or len(buttons) > 5:
            return False
        result = []
        for i in range(0, len(buttons)):
            result_buttons = []
            if len(buttons[i]) == 0 or len(buttons[i]) > 5:
                return False
            for k in range(0, len(buttons[i])):
                if buttons[i][k][0] and buttons[i][k][1]:
                    result_buttons.append({"text": buttons[i][k][0], "callback_data": buttons[i][k][1]})
            result.append(result_buttons)
        return {"inline_keyboard": result}
#    def ReplyKeyboardMarkup(self, buttons, resize_keyboard = False, one_time_keyboard = False, selective = False):
    def ReplyKeyboard(self, buttons, resize_keyboard = False, one_time_keyboard = False, selective = False):
#        """
#        ReplyKeyboardMarkup
#
#        buttons (array, Required) - buttons array
#        resize (resize_keyboard) (Boolean | Default: False) - Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons)
#        one_time (one_time_keyboard) (Boolean | Default: False) - Requests clients to hide the keyboard as soon as it's been used
#
#        Return
#
#        result (dict with array) - dict with array for 'reply_markup' Telegram API 'sendMessage'
#        """
        buttons_json = []
        for i in range(0, len(buttons)):
            if buttons[i][0]:
                button = {}
                button['text'] = buttons[i][0]
                buttons_json.append(button)
        result = {'keyboard': [buttons]}
        if resize_keyboard:
            result.update(resize_keyboard = True)
        if one_time_keyboard:
            result.update(one_time_keyboard = True)
        if selective:
            result.update(selective = True)
        return result
#    def KeyboardButton(self, buttons):
#        """
#        KeyboardButton
#
#        buttons (array, Required) - buttons array
#
#        Return
#
#        result (array) - buttons array
#        """
#        result = buttons
#        return result
    def ReplyKeyboardRemove(self, selective = None):
        """
        ReplyKeyboardRemove

        Nothing

        Return

        result (dict with array) - dict with array for 'reply_markup' Telegram API 'sendMessage'
        """
        result = {}
        result['remove_keyboard'] = True
        if selective:
            result['selective'] = selective
#        result = {'remove_keyboard': True}
        return result
    def sendSticker(self, id, sticker, reply_markup = None, disable_notification = None, reply_to_message_id = None):
        """
        sendSticker

        id (int, Required) - id chat
        sticker (string, Required) - a sticker
        reply_markup (array) - keyboard

        Return

        result (bool) - return Telegram API 'ok'
        """
        data = {}
        data['chat_id'] = id
        data['sticker'] = sticker
        if reply_markup:
            data['reply_markup'] = json.dumps(reply_markup)
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        send = requests.post(f'{self.request_url}/sendSticker', data = data)
        send_json = send.json()
        result = send_json['ok']
        return result
    def editMessageText(self, text, id = None, message_id = None, reply_markup = None, inline_message_id = None, \
    parse_mode = None, disable_web_page_preview = None):
        """
        editMessageText

        id (int, Required) - id chat
        message_id (int, Required)
        text (string, Required) - a new text
        reply_markup (array) - keyboard

        Return

        result (bool) - return Telegram API 'ok'
        """
        data = {}
        if id and message_id:
            data['chat_id'] = id
            data['message_id'] = message_id
        elif inline_message_id:
            data['inline_message_id'] = inline_message_id
        data['text'] = text
        if reply_markup:
            data['reply_markup'] = json.dumps(reply_markup)
        if parse_mode:
            data['parse_mode'] = parse_mode
        if disable_web_page_preview:
            data['disable_web_page_preview'] = disable_web_page_preview
        send = requests.post(f'{self.request_url}/editMessageText', data = data)
        send_json = send.json()
        result = send_json['ok']
        return result
    def editMessageReplyMarkup(self, reply_markup, id = None, message_id = None, inline_message_id = None):
        """
        editMessageText

        id (int, Required) - id chat
        message_id (int, Required)
        reply_markup (array, Required) - keyboard

        Return

        result (bool) - return Telegram API 'ok'
        """
        data = {}
        if id and message_id:
            data['chat_id'] = id
            data['message_id'] = message_id
        elif inline_message_id:
            data['inline_message_id'] = inline_message_id
        data['reply_markup'] = json.dumps(reply_markup)
        send = requests.post(f'{self.request_url}/editMessageReplyMarkup', data = data)
        send_json = send.json()
        result = send_json['ok']
        return result

if __name__ == '__main__':
    main()
