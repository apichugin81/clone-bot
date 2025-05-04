from aiogram import types

from src.constants import (
    ButtonText as BT,
    Markups
)

from src.base.nodes.node import Node


class GlassNodes:
    light_bulb = Node(
        text='Это лампочка/зеркало/градусник?',
        markup=Markups.YES_NO
    )

    dishware = Node(
        text='Это стеклянная посуда?',
        markup=Markups.YES_NO
    )

    is_dishware = Node(
        text='Посуда прозрачная?',
        markup=Markups.YES_NO
    )

    is_glass = Node(
        text='Принимается в ***Стекло***.\n'
             'Стекло делится по цветам на бесцветное, зелёное и коричневое.\n'
             'Перед сдачей нужно убрать все металлические части на горлышке (если есть).',
        markup=Markups.SORT_END
    )