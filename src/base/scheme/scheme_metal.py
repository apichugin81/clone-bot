import logging

from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


from src.constants import (
    ButtonText as BT,
)
from ..bot_settings import router
from ..nodes import MetalNodes as MN
from ..states import Metal


logging.basicConfig(level=logging.INFO)


@router.message(Metal.magnetic, F.text == BT.yes)
async def tin(message: Message, state: FSMContext):
    await state.set_state(Metal.tin)
    await MN.tin.write_back(message)


@router.message(Metal.magnetic, F.text == BT.no)
async def foil(message: Message, state: FSMContext):
    await state.set_state(Metal.foil)
    await MN.foil.write_back(message)


@router.message(Metal.foil, F.text == BT.yes)
async def crumples(message: Message, state: FSMContext):
    await state.set_state(Metal.crumples)
    await MN.crumples.write_back(message)


@router.message(Metal.foil, F.text == BT.no)
async def can(message: Message, state: FSMContext):
    await state.set_state(Metal.can)
    await MN.can.write_back(message)


@router.message(Metal.crumples, F.text == BT.yes)
async def is_foil(message: Message, state: FSMContext):
    await state.set_state(Metal.is_foil)
    await MN.is_foil.write_back(message)


@router.message(Metal.can, F.text == BT.yes)
async def is_can(message: Message, state: FSMContext):
    await state.set_state(Metal.is_can)
    await MN.is_can.write_back(message)


@router.message(Metal.can, F.text == BT.no)
async def spray_can(message: Message, state: FSMContext):
    await state.set_state(Metal.spray_can)
    await MN.spray_can.write_back(message)


@router.message(Metal.spray_can, F.text == BT.yes)
async def is_spray_can(message: Message, state: FSMContext):
    await state.set_state(Metal.is_spray_can)
    await MN.is_spray_can.write_back(message)


@router.message(Metal.spray_can, F.text == BT.no)
async def alu_pan(message: Message, state: FSMContext):
    await state.set_state(Metal.alu_pan)
    await MN.pan.write_back(message)


@router.message(Metal.alu_pan, F.text == BT.yes)
async def is_alu_pan(message: Message, state: FSMContext):
    await state.set_state(Metal.is_alu_pan)
    await MN.is_alu_pan.write_back(message)


@router.message(Metal.alu_pan, F.text == BT.no)
async def is_alu(message: Message, state: FSMContext):
    await state.set_state(Metal.is_alu)
    await MN.is_alu.write_back(message)


@router.message(Metal.tin, F.text == BT.yes)
async def is_tin(message: Message, state: FSMContext):
    await state.set_state(Metal.is_tin)
    await MN.is_tin.write_back(message)


@router.message(Metal.tin, F.text == BT.no)
async def iron_pan(message: Message, state: FSMContext):
    await state.set_state(Metal.iron_pan)
    await MN.pan.write_back(message)

@router.message(Metal.iron_pan, F.text == BT.no)
async def is_iron(message: Message, state: FSMContext):
    await state.set_state(Metal.is_iron)
    await MN.is_iron.write_back(message)

@router.message(Metal.iron_pan, F.text == BT.yes)
async def is_iron_pan(message: Message, state: FSMContext):
    await state.set_state(Metal.is_iron_pan)
    await MN.is_iron_pan.write_back(message)