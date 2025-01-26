from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import types, Router

from FirstLessonBot import keyboard

rout_fsm = Router()

class Registr(StatesGroup):
    name = State()
    number = State()


@rout_fsm.message(Command('reg'))
async def fsm_reg(message: types.Message, state: FSMContext):
    await state.set_state(Registr.name)
    await message.answer('Введите ваше имя:')

@rout_fsm.message(Registr.name)
async def fsm_reg_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registr.number)
    await message.answer('Введите ваш номер телефона: ', reply_markup=keyboard.kb_phone)

@rout_fsm.message(Registr.number)
async def fsm_reg_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Ваши данные:\n\n"
                         f"Имя: {data['name']}\n"
                         f"Номер телефона: {data['number']}\n"
                         f"Ваш id: {message.from_user.id}\n"
                         f"Ваш статус: {message.from_user.is_premium}")
    await state.clear()


