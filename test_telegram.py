#!/usr/bin/env python3
"""
Локальная проверка отправки сообщения в Telegram.
Запуск: python test_telegram.py
Установите переменные BOT_TOKEN и CHAT_ID перед запуском.
"""
import os
import sys

try:
    import requests
except ImportError:
    print("Установите requests: pip install requests")
    sys.exit(1)

# Укажите свои данные (или задайте через переменные окружения)
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВАШ_ТОКЕН_ОТ_BOTFATHER")
CHAT_ID = os.getenv("CHAT_ID", "ВАШ_ID_ОТ_USERINFOBOT")

if "ВАШ_" in BOT_TOKEN or "ВАШ_" in CHAT_ID:
    print("Задайте BOT_TOKEN и CHAT_ID:")
    print("  Windows: $env:BOT_TOKEN='токен'; $env:CHAT_ID='id'; python test_telegram.py")
    print("  Или отредактируйте переменные в скрипте")
    sys.exit(1)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "✅ Тест! Если вы видите это — бот работает.",
}

print(f"Отправка в chat_id={CHAT_ID}...")
response = requests.post(url, json=payload, timeout=10)

if response.status_code == 200:
    data = response.json()
    if data.get("ok"):
        print("✅ Сообщение отправлено! Проверьте Telegram.")
    else:
        print("❌ Ошибка API:", data)
else:
    print(f"❌ HTTP {response.status_code}:", response.text)
