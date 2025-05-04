# from aiogram import types
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from src.constants import (
    General_msg,
    Button,
    ButtonText as BT,
    Markups
)

from src.base.nodes.node import Node


class GeneralNodes:
    greet = Node(
        text=General_msg.greet_message,
        markup=(
            ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text=BT.start_sort)],
                          [KeyboardButton(text=BT.belka_tg)],
                          [KeyboardButton(text=BT.belka_vk)]],
                resize_keyboard=True, selective=True)
        )
    )

    start_sort = Node(
        text=General_msg.start_sort,
        markup=(
            ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text=BT.several_materials)],
                          [KeyboardButton(text=BT.paper), KeyboardButton(text=BT.plastic)],
                          [KeyboardButton(text=BT.metal), KeyboardButton(text=BT.glass)],
                          ],
                resize_keyboard=True, selective=True)
        )
    )

    separate = Node(
        text="Материалы можно отделить друг от друга?",
        markup=(
            ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text=BT.can), KeyboardButton(text=BT.cannot)],],
                resize_keyboard=True, selective=True)
        )
    )

    separable = Node(
        text="Нужно разделить на части и для каждой пройти тест отдельно",
        markup=(
            ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text=BT.start_sort)]],
                resize_keyboard=True, selective=True)
            # .add(BT.start_sort)
        )
    )

    battery_or_technique = Node(
        text="Это техника или батарейка?",
        markup=(
            ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text=BT.technique), KeyboardButton(text=BT.battery)],
                          [KeyboardButton(text=BT.not_technique)]],
                resize_keyboard=True, selective=True)
        )
    )

    is_battery = Node(
        text='Принимается на акции во фракцию ***Батарейки***.',
        markup=Markups.SORT_END
    )

    is_technique = Node(
        text='Принимается на акции во фракцию ***Техника***.',
        markup=Markups.SORT_END
    )

    is_trash = Node(
        text='Не принимается на акции.',
        markup=Markups.SORT_END
    )

    sort_again = Node(
        text='Отлично! Хочешь посортировать ещё?',
        markup=(
            ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text=BT.start_sort)]],
                resize_keyboard=True, selective=True)
        )
    )

    belka_vk = Node(
        text='Чтобы перейти в группу, нажми на кнопку ниже',
        markup=(
            InlineKeyboardMarkup(
                inline_keyboard=[[Button.belka_vk]],
                resize_keyboard=True, selective=True)
        )
    )

    belka_tg = Node(
        text='Чтобы перейти в группу, нажми на кнопку ниже',
        markup=(
            InlineKeyboardMarkup(
                inline_keyboard=[[Button.belka_tg]],
                resize_keyboard=True, selective=True)
        )
    )
