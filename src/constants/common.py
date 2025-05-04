# Основные константы для проекта
from aiogram import types

API_TOKEN = '6547554591:AAFHMXCn0ues0CM2DaUR595ZbOFA2lAcyAQ'


class URL:
    prozero_tg = "https://t.me/prozero_eco"
    prozero_vk = ""  # TODO
    greenbelka_tg = "https://t.me/greenbelka"
    greenbelka_vk = "https://vk.com/eco_week"


class General_msg:
    greet_message = f'Привет! Я — бот Зелёной белки, и я помогу тебе рассортировать вторсырьё.'
    start_sort = "Возьми предмет, который хочешь сдать на переработку и отвечай на мои вопросы.\n\n" \
                 "Из какого материала сделан предмет, который ты хочешь сдать?"
