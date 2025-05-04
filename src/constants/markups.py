from aiogram import types
from aiogram.types import KeyboardButton

from .buttons import ButtonText as BT


class Markups:
    SORT_END = (
        types.ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=BT.back_main_menu)],
                      [KeyboardButton(text=BT.start_sort)]],
            resize_keyboard=True, selective=True)
    )

    YES_NO = (
        types.ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text=BT.yes), KeyboardButton(text=BT.no)]],
            resize_keyboard=True, selective=True)
    )
