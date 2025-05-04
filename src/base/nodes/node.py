# Скрипт с основным кодом.
# Здесь не должно быть текстов сообщений. Все тексты сообщений считаем константами и выносим с constants/messages


import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputMediaPhoto
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.enums import ParseMode
from aiogram.fsm.state import State, StatesGroup

from src.constants.common import (
    API_TOKEN,
    URL,
    General_msg,
)

bot = Bot(token=API_TOKEN)


class Node:
    def __init__(self, text, markup=None, photo_id=None, album=None):
        self.text = text
        if markup == None:
            self.markup = types.ReplyKeyboardRemove()
        else:
            self.markup = markup
        self.photo_id = photo_id
        self.album = album

    async def write_back(self, message):
        if self.photo_id != None:
            await bot.send_photo(
                message.chat.id,
                self.photo_id,
                caption=self.text,
                reply_markup=self.markup,
                parse_mode=ParseMode.MARKDOWN
            )
        elif self.album != None:
            await bot.send_media_group(
                message.chat.id,
                self.album,
            )
            await bot.send_message(
                message.chat.id,
                md.text(self.text, sep='\n\n'),
                reply_markup=self.markup,
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await bot.send_message(
                message.chat.id,
                md.text(self.text, sep='\n\n'),
                reply_markup=self.markup,
                parse_mode=ParseMode.MARKDOWN
            )


def start_func(message):
    greet_message = f'Привет, {message.from_user.first_name} {message.from_user.last_name}!' \
                    f' Я - бот Зелёной белки, и я помогу тебе рассортировать вторсырьё.'
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Начать сортировку", callback_data='начало сортировки'))
    markup.add(types.InlineKeyboardButton("Перейти в группу зелёной белки ТГ", url=URL.greenbelka_tg))
    markup.add(types.InlineKeyboardButton("Перейти в группу зелёной белки ВК", url=URL.greenbelka_vk))
    bot.send_message(message.chat.id, greet_message, parse_mode='html', reply_markup=markup)
