from aiogram import Router, types, html, F
from aiogram.filters import Command, CommandObject
from aiogram.enums import ParseMode
from aiogram.types import (BufferedInputFile, FSInputFile, URLInputFile,
                           CallbackQuery)
from aiogram.utils.media_group import MediaGroupBuilder

from FirstLessonBot import keyboard


TEXT = """
/start - запуск бота
/help - помощь
/set_argument <name> <age> <city> - установить аргумент
"""
TEXT_ARG = """
Аргумент должен быть такого типа:

/set_argument <name> <age> <city>
"""

rout_handlers = Router()

@rout_handlers.message(F.text == '/start')
async def hand_mes(message: types.Message):
    await message.answer(f'Привет, {html.bold(message.from_user.full_name)}🔥!',
                         parse_mode=ParseMode.HTML,
                         reply_markup=keyboard.inline_key_one)

@rout_handlers.message(F.text == '/f_photo')
async def fs_photo_message(message: types.Message):
    photo_fs = FSInputFile('source/cosmos.jpg')
    await message.answer_photo(photo_fs)

@rout_handlers.message(F.text == '/u_photo')
async def url_photo_message(message: types.Message):
    photo_url = URLInputFile('https://avatars.mds.yandex.net/get-mpic/4489193/img_id7920284593202388608.jpeg/orig')
    await message.answer_photo(photo_url, caption='<i>Это мое фото!</i>', parse_mode=ParseMode.HTML)

@rout_handlers.message(F.text == '/b_photo')
async def buf_photo_message(message: types.Message):
    with open('source/cosmos.jpg', 'rb') as photo:
        await message.answer_photo(BufferedInputFile(file=photo.read(),
                                                     filename='My photo!'),
                                   caption='<b>MY PHTOOTOT!</b>',
                                   parse_mode=ParseMode.HTML)

@rout_handlers.message(F.text == '/local')
async def location_message(message: types.Message):
    await message.answer_location(54.177263, 37.651394)


@rout_handlers.message(F.text == '/media')
async def media_message(message: types.Message):
    photo1 = FSInputFile('source/cosmos.jpg')
    photo2 = FSInputFile('source/image_2.jpg')
    video1 = FSInputFile('source/IMG_7237.MP4')
    media = MediaGroupBuilder(caption='Моя подборка!')
    media.add_photo(photo1)
    media.add_photo(photo2)
    media.add_video(video1)
    await message.answer_media_group(media.build())

@rout_handlers.message(F.text == '/audio')
async def audio_message(message: types.Message):
    aud1 = FSInputFile('source/Platina.mp3')
    await message.answer_audio(aud1)

@rout_handlers.message(F.text == '/sticker')
async def sticker_message(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAENTiBnWL7gULTItc8v7uKC3f2dcq2I-QACFgADwDZPE2Ah1y2iBLZnNgQ')

@rout_handlers.message(F.text == '/help')
async def command_help(message: types.Message):
    await message.reply(TEXT)

@rout_handlers.message(F.text == '/set_argument')
async def argument_user(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer('Вы не ввели аргумент!')
        return

    try:
        name, age, city = command.args.split(' ')

    except ValueError:
        await message.answer(TEXT_ARG)
        return

    await message.answer(f"Ваше имя: {name},\n"
                         f"Ваш возраст: {age},\n"
                         f"Ваш город: {city}.")

@rout_handlers.callback_query(F.data == 'google')
async def cb_google_handler(callback: CallbackQuery):
    await callback.answer('Вы выбрали goole', show_alert=True)
    await callback.message.answer('WAAAAU', reply_markup= await keyboard.cars_handler())

# @rout_handlers.message()
# async def echo_message(message: types.Message):
#     await message.reply(message.text)

