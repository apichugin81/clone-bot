from aiogram import types

from src.constants import (
    Button,
    ButtonText as BT,
)

from src.base.nodes.node import Node


class PlasticNodes:
    cap = Node(
        text='',
        markup=(
            types.ReplyKeyboardMarkup(
                keyboard=[[]],
                resize_keyboard=True, selective=True)
        )
    )