# Скрипт с основным кодом.
# Здесь не должно быть текстов сообщений. Все тексты сообщений считаем константами и выносим в constants/messages

import logging

import asyncio
from aiogram import types, F
from aiogram.types import Message, ReplyKeyboardRemove

from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart

from src.constants import (ButtonText as BT)
from src.base.bot_settings import router, dp, bot
from src.base.nodes import (
    GeneralNodes as GN,
    MetalNodes as MN,
    PlasticNodes as PN,
    PaperNodes,
    GlassNodes,
)
from src.base.states import *
from src.base.scheme import *

logging.basicConfig(level=logging.INFO)


@router.message(CommandStart())
# @dp.message(lambda message: message.text.lower().strip() in
#                                     [BT.back_main_menu.lower(), BT.main_menu.lower()], state='*')
@router.message(F.text.casefold() == "start")
@router.message(F.text.capitalize().in_([BT.back_main_menu, BT.main_menu]))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(General.start)
    await GN.greet.write_back(message)


@router.message(General.start, F.text == BT.belka_tg)
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(General.start)
    await GN.belka_tg.write_back(message)


@router.message(F.photo)
async def add_photo(message: Message, state: FSMContext):
    print(message.photo[-1].file_id)


@router.message(General.start, F.text == BT.belka_vk)
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(General.start)
    await GN.belka_vk.write_back(message)


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(F.text.capitalize() == BT.start_sort)
async def start_sort(message: types.Message, state: FSMContext):
    await state.set_state(General.material)
    await GN.start_sort.write_back(message)


@router.message(General.material, F.text.capitalize() == BT.several_materials)
async def several_materials(message: types.Message, state: FSMContext):
    await state.set_state(General.separable)
    await GN.separate.write_back(message)


@router.message(General.separable, F.text.capitalize() == BT.can)
async def separable(message: types.Message, state: FSMContext):
    await state.set_state(General.start)
    await GN.separable.write_back(message)


@router.message(General.separable, F.text.capitalize() == BT.cannot)
async def not_separable(message: types.Message, state: FSMContext):
    await state.set_state(General.battery_or_technique)
    await GN.battery_or_technique.write_back(message)


@router.message(General.battery_or_technique, F.text.capitalize() == BT.battery)
async def is_battery(message: types.Message, state: FSMContext):
    await state.set_state(General.main_menu)
    await GN.is_battery.write_back(message)


@router.message(General.battery_or_technique, F.text.capitalize() == BT.technique)
async def is_technique(message: types.Message, state: FSMContext):
    await state.set_state(General.main_menu)
    await GN.is_technique.write_back(message)


@router.message(General.material, F.text.capitalize() == BT.metal)
async def magnetic(message: types.Message, state: FSMContext):
    await state.set_state(Metal.magnetic)
    await MN.magnetic.write_back(message)


@router.message(General.material, F.text.capitalize() == BT.plastic)
async def small_plastic(message: types.Message, state: FSMContext):
    await state.set_state(Plastic.cap)
    await PN.cap.write_back(message)

@router.message(General.material, F.text.capitalize() == BT.paper)
async def pulperboard(message: types.Message, state: FSMContext):
    await state.set_state(Paper.pulperboard)
    await PaperNodes.pulperboard.write_back(message)

@router.message(General.material, F.text.capitalize() == BT.glass)
async def light_bulb(message: types.Message, state: FSMContext):
    await state.set_state(Glass.light_bulb)
    await GlassNodes.light_bulb.write_back(message)

@router.message(General.battery_or_technique, F.text.capitalize() == BT.not_technique)  # не разделяющиеся части
@router.message(Metal.crumples, F.text.capitalize() == BT.no)  # пластик как фольга
@router.message(Paper.napkin, F.text.capitalize() == BT.yes)  # одноразовая салфетка
@router.message(Paper.lamination, F.text.capitalize() == BT.yes)  # бумага с ламинацией
@router.message(Paper.oil, F.text.capitalize() == BT.yes)  # бумага с пятнами жира
@router.message(Paper.receipt, F.text.capitalize() == BT.yes)  # кассовый чек
@router.message(Glass.light_bulb, F.text.capitalize() == BT.yes)  # лампочка или градусник
@router.message(Glass.dishware, F.text.capitalize() == BT.no)  # стекл. посуда
async def is_trash(message: types.Message, state: FSMContext):
    await state.set_state(General.main_menu)
    await GN.is_trash.write_back(message)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
