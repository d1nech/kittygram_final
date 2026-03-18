#!/usr/bin/env python3
"""
Получить chat_id из обновлений бота.
1. Напишите вашему боту /start в Telegram
2. Сразу запустите: python get_telegram_chat_id.py
"""
import os
import sys

try:
    import requests
except ImportError:
    print("Установите requests: pip install requests")
    sys.exit(1)

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
if not BOT_TOKEN:
    print("Задайте BOT_TOKEN: $env:BOT_TOKEN='ваш_токен'")
    sys.exit(1)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
print("Запрос обновлений бота...")
print("(Убедитесь, что вы только что написали /start боту)\n")

response = requests.get(url, timeout=15)
data = response.json()

if not data.get("ok"):
    print("Ошибка:", data)
    sys.exit(1)

results = data.get("result", [])
if not results:
    print("Нет обновлений. Напишите боту /start и запустите скрипт снова.")
    sys.exit(1)

# Берём последнее сообщение
last = results[-1]
chat = last.get("message", {}).get("chat", {})
chat_id = chat.get("id")
username = chat.get("username", "?")

print(f"Chat ID: {chat_id}")
print(f"Username: @{username}")
print(f"\nИспользуйте в GitHub Secrets: TELEGRAM_CHAT_ID = {chat_id}")
