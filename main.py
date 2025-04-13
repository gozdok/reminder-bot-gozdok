import telebot
import time
import random
from datetime import datetime, timedelta
import pytz

TOKEN = "7762206409:AAFePy9OGuJWG-HxB48JRoKc1f6VFa4IRYc"
CHAT_ID = 312503925
bot = telebot.TeleBot(TOKEN)

tz = pytz.timezone("Europe/Moscow")

def send_task(task_name, task_description):
    try:
        bot.send_message(CHAT_ID, f"{task_name}\n{task_description}")
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")

def wait_until(target_time):
    now = datetime.now(tz)
    wait_seconds = (target_time - now).total_seconds()
    if wait_seconds > 0:
        time.sleep(wait_seconds)

def get_random_time(start_hour, end_hour):
    now = datetime.now(tz)
    random_minutes = random.randint(0, (end_hour - start_hour) * 60)
    return now.replace(hour=start_hour, minute=0, second=0, microsecond=0) + timedelta(minutes=random_minutes)

def main():
    print("Бот запущен.")
    
    # Утренняя привычка
    morning_time = datetime.now(tz).replace(hour=9, minute=0, second=0, microsecond=0)
    wait_until(morning_time)
    send_task("Утренняя привычка — Утренняя настройка", 
              "Оцени своё настроение, подумай, что важно сегодня, и поставь 1 цель на день.")

    # 1 минута тишины
    silence_time = get_random_time(12, 20)
    wait_until(silence_time)
    send_task("1 минута тишины", 
              "Сядь в тишине на одну минуту. Без экрана, без мыслей. Просто подыши и замри.")

    # 25 минут на задачу
    focus_time = get_random_time(15, 20)
    wait_until(focus_time)
    send_task("25 минут на задачу", 
              "Выбери одну небольшую задачу и сфокусируйся на ней 25 минут. Никаких отвлечений.")

    # 5-минутное правило
    five_min_time = get_random_time(12, 20)
    wait_until(five_min_time)
    send_task("5-минутное правило", 
              "Если что-то можно сделать за 5 минут — сделай это прямо сейчас.")

    # Комментарий дня
    comment_time = datetime.now(tz).replace(hour=22, minute=0, second=0, microsecond=0)
    wait_until(comment_time)
    send_task("Комментарий дня", 
              "Напиши короткий комментарий для себя: как прошёл день, что почувствовал(а), чему научился(ась).")

if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            print(f"Ошибка: {e}. Перезапуск через 10 секунд.")
            time.sleep(10)
