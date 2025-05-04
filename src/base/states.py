# Набор всех состояний для бота

from aiogram.fsm.state import State, StatesGroup


class General(StatesGroup):
    start = State()
    material = State()
    separable = State()
    battery_or_technique = State()
    is_battery_or_technique = State()
    main_menu = State()
    belka_tg = State()
    belka_vk = State()


class Metal(StatesGroup):
    magnetic = State()

    foil = State()
    crumples = State()
    can = State()
    is_foil = State()
    is_can = State()
    spray_can = State()
    is_spray_can = State()
    alu_pan = State()
    is_alu_pan = State()
    is_alu = State()

    tin = State()
    is_tin = State()
    iron_pan = State()
    is_iron_pan = State()
    is_iron = State()


class Paper(StatesGroup):
    pulperboard = State()
    is_pulperboard = State()
    napkin = State()
    lamination = State()
    oil = State()
    receipt = State()
    is_paper = State()


class Glass(StatesGroup):
    light_bulb = State()
    dishware = State()
    is_glass = State()
    is_dishware = State()
    is_opaque_dishware = State()


class Plastic(StatesGroup):
    cap = State()
    pet = State()
    pnd = State()

