import telebot
import time
import random
from datetime import datetime, timedelta
import pytz

TOKEN = "7762206409:AAFePy9OGuJWG-HxB48JRoKc1f6VFa4IRYc"
CHAT_ID = 312503925

bot = telebot.TeleBot(TOKEN)
tz = pytz.timezone("Europe/Moscow")

# Уведомление при запуске
bot.send_message(CHAT_ID, "Бот успешно запущен и ожидает отправки задач.")

def send_message(task_name, task_description):
    bot.send_message(CHAT_ID, f"{task_name}\n{task_description}")

def wait_until(target_time):
    now = datetime.now(tz)
    delta = (target_time - now).total_seconds()
    if delta > 0:
        time.sleep(delta)

def get_random_time(start_hour, end_hour):
    now = datetime.now(tz)
    random_hour = random.randint(start_hour, end_hour - 1)
    random_minute = random.randint(0, 59)
    target_time = now.replace(hour=random_hour, minute=random_minute, second=0, microsecond=0)
    if target_time < now:
        target_time += timedelta(days=1)
    return target_time

def schedule_task(name, description, hour=None, minute=None, random_range=None):
    if hour is not None and minute is not None:
        target_time = datetime.now(tz).replace(hour=hour, minute=minute, second=0, microsecond=0)
        if target_time < datetime.now(tz):
            target_time += timedelta(days=1)
    elif random_range:
        target_time = get_random_time(*random_range)
    else:
        return

    wait_until(target_time)
    send_message(name, description)

while True:
    now = datetime.now(tz)

    # Утренний Вектор — 9:00
    if now.hour == 8 and now.minute == 59:
        schedule_task(
            "Утренний Вектор (в 9:00)",
            "Запиши свои цели на день. Что важно сделать? Какие три вещи сделают день продуктивным?"
        )

    # Комментарий дня — 22:00
    elif now.hour == 21 and now.minute == 59:
        schedule_task(
            "Комментарий дня (в 22:00)",
            "Подведи итоги: что получилось, чему научился, за что себя хвалишь?"
        )

    # Случайные задачи
    elif now.hour == 11 and now.minute == 59:
        schedule_task(
            "Одна минута тишины",
            "Остановись на минуту. Сделай глубокий вдох. Побудь в тишине. Перезагрузись.",
            random_range=(12, 20)
        )

        schedule_task(
            "25 минут на задачу",
            "Сфокусируйся на одной важной задаче и работай над ней 25 минут без отвлечений.",
            random_range=(15, 20)
        )

        schedule_task(
            "Правило 5 минут",
            "Начни делать задачу, которую откладывал. Потрать всего 5 минут — и посмотри, захочешь ли продолжить.",
            random_range=(12, 20)
        )

    time.sleep(60)
