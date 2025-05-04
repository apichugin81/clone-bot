import logging

from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from src.constants import (
    ButtonText as BT,
)
from ..bot_settings import router
from ..nodes import GlassNodes as GN
from ..states import Glass


logging.basicConfig(level=logging.INFO)


@router.message(Glass.light_bulb, F.text == BT.no)
async def dishware(message: Message, state: FSMContext):
    await state.set_state(Glass.dishware)
    await GN.dishware.write_back(message)

@router.message(Glass.dishware, F.text == BT.no)
async def is_glass(message: Message, state: FSMContext):
    await state.set_state(Glass.is_glass)
    await GN.is_glass.write_back(message)

@router.message(Glass.dishware, F.text == BT.yes)
async def is_dishware(message: Message, state: FSMContext):
    await state.set_state(Glass.is_dishware)
    await GN.is_dishware.write_back(message)

# @router.message(Glass.dishware, F.text == BT.yes)
# async def is_dishware(message: Message, state: FSMContext):
#     await state.set_state(Glass.is_dishware)
#     await GN.is_dishware.write_back(message)