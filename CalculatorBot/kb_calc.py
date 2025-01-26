from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_number_main=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3')],
    [KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='6')],
    [KeyboardButton(text='7'), KeyboardButton(text='8'), KeyboardButton(text='9')],
    [KeyboardButton(text='Exit'), KeyboardButton(text='0'), KeyboardButton(text='>')]],
    resize_keyboard=True,
    input_field_placeholder='Ожидание выражений...')