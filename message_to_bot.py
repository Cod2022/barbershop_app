import requests
from dotenv import load_dotenv
import os
from os.path import join, dirname

def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


def send_message(chat_id, text):
    method = 'sendMessage'
    token = get_from_env('BOT_TOKEN')
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

if __name__ == '__main__':
    name = "Имя Фамилия"
    phone = "+79876784325"
    new_client = f"Новый клиент: {name}, {phone}"
    send_message(get_from_env('CHAT_ID'), new_client)
    