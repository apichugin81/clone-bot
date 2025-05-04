from aiogram import types

from src.constants import (
    ButtonText as BT,
    Markups
)

from src.base.nodes.node import Node


class MetalNodes:
    magnetic = Node(
        text='Предмет магнитится?',
        markup=Markups.YES_NO
    )

    tin = Node(
        text='Это консервная банка/закатывающаяся крышка от солений?',
        markup=Markups.YES_NO
    )

    foil = Node(
        text='Это фольга?',
        markup=Markups.YES_NO
    )

    crumples = Node(
        text='Если смять, остаётся смятой?',
        markup=Markups.YES_NO
    )

    can = Node(
        text='Это алюминиевая банка из-под напитка?',
        markup=Markups.YES_NO
    )

    is_foil = Node(
        text='Принимается на акции во фракцию ***Алюминиевая фольга***',
        markup=Markups.SORT_END
    )

    is_can = Node(
        text='Принимается на акции во фракцию ***Алюминиевая банка***.\n'
             'Перед сдачей лучше смять',
        markup=Markups.SORT_END
    )

    spray_can = Node(
        text='Это баллон под давлением?',
        markup=Markups.YES_NO
    )

    is_spray_can = Node(
        text='Принимается в ***Алюминий прочий***.\n'
             'Перед сдачей баллон нужно проткнуть.',
        markup=Markups.SORT_END
    )

    pan = Node(
        text='Это сковорода или кастрюля?',
        markup=Markups.YES_NO
    )

    is_alu_pan = Node(
        text='Принимается в ***Алюминий прочий***.\n'
             'Перед сдачей нужно убрать все пластиковые ручки.',
        markup=Markups.SORT_END
    )

    is_alu = Node(
        text='Принимается в ***Алюминий прочий***.',
        markup=Markups.SORT_END
    )

    is_tin = Node(
        text='Принимается в ***Жесть консервная***.\n'
             'Перед сдачей лучше смять, можете воспользоваться нашим лайфхаком.',
        markup=Markups.SORT_END,
        photo_id='AgACAgIAAxkBAAIF0WcmM1JUeMlQnlyM-QulqpNQTNgpAAIQ3zEbzCAwSa_IOql-KHR8AQADAgADeQADNgQ',
    )

    is_iron_pan = Node(
        text='Принимается в ***Жесть прочая***.\n'
             'Перед сдачей нужно убрать все пластиковые ручки.',
        markup=Markups.SORT_END
    )

    is_iron = Node(
        text='Принимается в ***Жесть прочая***.',
        markup=Markups.SORT_END
    )