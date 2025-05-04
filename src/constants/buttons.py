from aiogram.types.inline_keyboard_button import InlineKeyboardButton

from .common import URL


class ButtonText:
    start_sort = "Начать сортировку"
    main_menu = "Главное меню"
    back_main_menu = "Вернуться в главное меню"
    yes = 'Да'
    no = 'Нет'

    belka_tg = "Перейти в группу зелёной белки ТГ"
    belka_vk = "Перейти в группу зелёной белки ВК"

    several_materials = "Из нескольких материалов/частей"
    can = 'Можно'
    cannot = 'Нельзя'
    technique = 'Техника'
    battery = 'Батарейка'
    not_technique = 'Не техника и не батарейка'

    metal = 'Металл'

    plastic = 'Пластик'

    glass = 'Стекло'

    paper = 'Бумага'


class Button:
    belka_tg = InlineKeyboardButton(text=ButtonText.belka_tg, url=URL.greenbelka_tg)
    belka_vk = InlineKeyboardButton(text=ButtonText.belka_vk, url=URL.greenbelka_vk)


print()