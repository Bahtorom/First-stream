
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from YouTubeBot import keyboards
import YouTubeBot.database.requests as req


router_youtube = Router()

@router_youtube.message(CommandStart())
async def yt_start(msg: Message):
    await req.set_user(msg.from_user.id)
    await msg.answer('Добро пожаловать в магазин кроссовок!', reply_markup=keyboards.kb_main)

@router_youtube.message(F.text == 'Каталог')
async def catalog(msg: Message):
    await msg.answer('Выберите категорию товара', reply_markup= await keyboards.categories())

@router_youtube.callback_query(F.data == 'to_main')
async def callback_to_main(callback: CallbackQuery):
    await callback.answer('Вы перешли в меню!')
    await callback.message.answer('Меню:', reply_markup=keyboards.kb_main)



@router_youtube.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup= await keyboards.items(callback.data.split('_')[1]))

@router_youtube.callback_query(F.data.startswith('item_'))
async def items(callback: CallbackQuery):
    item_data = await req.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\n'
                                  f'Описание: {item_data.description}\n'
                                  f'Цена: {item_data.price} P',
                                  reply_markup= await keyboards.items(callback.data.split('_')[1]))


