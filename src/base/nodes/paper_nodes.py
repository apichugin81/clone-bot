from pickletools import markobject

from aiogram.types import InputMediaPhoto

from src.constants import (
    Button,
    ButtonText as BT,
    MSG,
)

from src.constants.markups import Markups

from src.base.nodes.node import Node


class PaperNodes:
    pulperboard = Node(
        text='Это втулки (внутренности рулонов от туалетной бумаги, скотча, бум. полотенец и проч.) '
             'или упаковки от яиц и подобные им (см. примеры на фото выше)?',
        markup=Markups.YES_NO,
        album=[
            InputMediaPhoto(
                type='photo',
                media='AgACAgIAAxkBAAIGHWcmPSzihDiNOM1K4wy0YOOiBvoPAAJ33zEbzCAwScIUfMRK9MjtAQADAgADeQADNgQ',
            ),
            InputMediaPhoto(
                type='photo',
                media='AgACAgIAAxkBAAIGHGcmPRMIoBBrvJ6kLhFAPCJXSx0KAAJ13zEbzCAwSdWDitJp8khIAQADAgADeQADNgQ'),
        ],
    )

    is_pulperboard = Node(
        text=MSG.prozero_text,
        markup=Markups.SORT_END
    )

    napkin = Node(
        text='Это бумага одноразового пользования (салфетки, туалетная бумага)?',
        markup=Markups.YES_NO
    )

    lamination = Node(
        text='На бумаге есть ламинация (плёнка, проверяется на надрыв, см. фото)?',
        markup=Markups.YES_NO,
        photo_id='AgACAgIAAxkBAAIGv2dsEl2TdJErllsUJJNK7Pqx6kYqAALK5DEbah1hS0Ab_MdN_eD0AQADAgADeQADNgQ'
    )

    oil = Node(
        text='На бумаге есть пятна жира?',
        markup=Markups.YES_NO
    )

    receipt = Node(
        text='Это кассовый чек/пергамент/калька?',
        markup=Markups.YES_NO
    )

    is_paper = Node(
        text='Принимается в ***Макулатуру***.\n'
             'Перед сдачей хорошо упаковать в коробку или пакет, чтобы ничего не высыпалось.',
        markup=Markups.SORT_END
    )
