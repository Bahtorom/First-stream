
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from CalculatorBot.kb_calc import kb_number_main
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class Numb(StatesGroup):
    number = State()

router_calc = Router()

@router_calc.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Здравствуй дорогой, <b>{message.from_user.first_name}</b>!\n\n"
                         f"Ниже по списку представленны действующие функции это Бота:\n"
                         f"1. Калькулятор - /CalculatorBot\n"
                         f"2. <i>в разработке...</i>", parse_mode=ParseMode.HTML)

# @router_calc.message(Command('CalculatorBot'))
# async def calc_menu(message: Message):
#     await message.answer(text='Вы находитесь в Калькуляторе!',
#                          reply_markup=kb_number_main)
#     print(message.text)

@router_calc.message(Command('CalculatorBot'))
async def calc_fsm(message: Message, state: FSMContext):
    await state.set_state(Numb.number)
    await message.answer('Введите выражение:')

@router_calc.message(Numb.number)
async def calc_answer(message: Message, state:FSMContext):
    await state.update_data(number=eval(message.text))
    data = await state.get_data()
    await message.answer(f"Ваш ответ: {data['number']}")
    await state.clear()