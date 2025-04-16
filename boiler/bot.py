# import telebot
# from boiler.models import AllowedTelegramUser, ContactMessage
# from django.utils import timezone
#
# bot = telebot.TeleBot('7833910204:AAGamUBw7ujcgEV7LLq8Uxz555-8HR5ZICE')
#
# # Команда для просмотра сообщений
# @bot.message_handler(commands=['messages'])
# def get_messages(message):
#     chat_id = message.chat.id
#     username = message.from_user.username  # Получаем username пользователя
#
#     # Проверяем, есть ли у пользователя доступ
#     if not AllowedTelegramUser.objects.filter(username=username).exists():
#         bot.send_message(chat_id, "⛔ У вас нет доступа к сообщениям.")
#         return
#
#     # Получаем последние сообщения
#     messages = ContactMessage.objects.all().order_by('-created_at')[:5]
#
#     if not messages:
#         bot.send_message(chat_id, "Сообщений пока нет.")
#         return
#
#     # Отправляем сообщения пользователю
#     for msg in messages:
#         bot.send_message(chat_id, f"""
# <b>📨 Новое сообщение</b>
# 👤 {msg.name}
# 📧 {msg.email}
# 💬 {msg.message}
# 🕒 {msg.created_at.strftime("%d.%m.%Y %H:%M")}
# """, parse_mode="HTML")
#
# # Запуск бота
# bot.polling()

import telebot
from boiler.models import TelegramUser

bot = telebot.TeleBot('7833910204:AAGamUBw7ujcgEV7LLq8Uxz555-8HR5ZICE')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    username = message.chat.username
    first_name = message.chat.first_name

    # Проверяем, есть ли уже этот пользователь в базе данных
    user, created = TelegramUser.objects.get_or_create(
        chat_id=chat_id,
        defaults={'username': username, 'first_name': first_name}
    )

    if created:
        # Если пользователь только что добавился
        bot.send_message(chat_id, "Спасибо за регистрацию. Мы запомнили твой chat_id!")

    # Если пользователь в админке, отправляем сообщение
    if user.is_admin:
        bot.send_message(chat_id, "Ты администратор! Я могу отправить сообщение от твоего имени.")
    else:
        bot.send_message(chat_id, "Ты не администратор, поэтому не могу отправить сообщение.")

# Запуск бота
bot.polling()

