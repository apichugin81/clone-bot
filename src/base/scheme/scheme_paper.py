import logging

from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from src.constants import (
    ButtonText as BT,
)
from ..bot_settings import router
from ..nodes import PaperNodes as PN
from ..states import Paper


logging.basicConfig(level=logging.INFO)


@router.message(Paper.pulperboard, F.text == BT.yes)
async def is_pulperboard(message: Message, state: FSMContext):
    await state.set_state(Paper.is_pulperboard)
    await PN.is_pulperboard.write_back(message)

@router.message(Paper.pulperboard, F.text == BT.no)
async def napkin(message: Message, state: FSMContext):
    await state.set_state(Paper.napkin)
    await PN.napkin.write_back(message)

@router.message(Paper.napkin, F.text == BT.no)
async def lamination(message: Message, state: FSMContext):
    await state.set_state(Paper.lamination)
    await PN.lamination.write_back(message)

@router.message(Paper.lamination, F.text == BT.no)
async def oil(message: Message, state: FSMContext):
    await state.set_state(Paper.oil)
    await PN.oil.write_back(message)

@router.message(Paper.oil, F.text == BT.no)
async def receipt(message: Message, state: FSMContext):
    await state.set_state(Paper.receipt)
    await PN.receipt.write_back(message)

@router.message(Paper.receipt, F.text == BT.no)
async def is_paper(message: Message, state: FSMContext):
    await state.set_state(Paper.is_paper)
    await PN.is_paper.write_back(message)