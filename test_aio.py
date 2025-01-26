from aiogram import types, Bot, Dispatcher, Router
from config import TOKEN
from aiogram.filters import Command
from aiogram.types import audio, Audio, Message, FSInputFile, BackgroundFillFreeformGradient
import asyncio
import logging

router = Router()


@router.message(Command('start'))
async def hand_mes_aud(msg: Message):

    await msg.answer(text='Hellp')



async def main():
    bot = Bot(token=TOKEN)
    
    dp =Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')

