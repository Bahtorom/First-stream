from aiogram.types import (KeyboardButton, InlineKeyboardMarkup,
                           InlineKeyboardButton, ReplyKeyboardMarkup)

from aiogram.utils.keyboard import InlineKeyboardBuilder

keyboard_one = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/help'), KeyboardButton(text='/audio')],
    [KeyboardButton(text='/start'), KeyboardButton(text='/f_photo')]],
                                    resize_keyboard=True,
                                    one_time_keyboard=True
                                    )

inline_key_one = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Google', callback_data='google')],
    [InlineKeyboardButton(text='Yandex', callback_data='yandex')]
])

kb_phone = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить свой номер', request_contact= True)]])

cars = ['Mercedes', 'Porsche', 'Lada', 'Audi']

async def cars_handler():
    keyb = InlineKeyboardBuilder()
    for car in cars:
        keyb.add(InlineKeyboardButton(text=car, url=f'https://google.com/search?q={car}'))
    return keyb.adjust(2).as_markup()



