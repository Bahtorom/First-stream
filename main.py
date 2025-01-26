from aiogram import Dispatcher, Bot, F, types
import asyncio
from config import TOKEN
import logging
from YouTubeBot.handlers import router_youtube
from YouTubeBot.fsm import router_fsm_yb
from YouTubeBot.database.models import async_main

bot = Bot(TOKEN)
dp = Dispatcher()




async def main():

    await async_main()
    dp.include_router(router_youtube)
    dp.include_router(router_fsm_yb)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print('exit')



