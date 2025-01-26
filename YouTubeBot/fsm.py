from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command


router_fsm_yb = Router()

class Reg(StatesGroup):
    name = State()
    age = State()
    number = State()


@router_fsm_yb.message(Command('register'))
async def register_handler(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите ваше имя:')

@router_fsm_yb.message(Reg.name)
async def reg_name_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.age)
    await message.answer('Введите ваш возраст:')

@router_fsm_yb.message(Reg.age)
async def reg_age_handler(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Reg.number)
    await message.answer('Отправте ваш номер телефона:', reply_markup=get_contact)

@router_fsm_yb.message(Reg.number, F.contact)
async def reg_number_handler(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer('Ваши данные:\nИмя: %s\nВозраст: %s\nНомер: %s' % (data['name'], data['age'], data['number']))
    await state.clear()