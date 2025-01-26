from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand,BotCommandScopeDefault, BotDescription
from config import TOKEN
import asyncio
import logging
from FirstLessonBot.handlers import rout_handlers


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def menu_commands():
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='help', description='Помощь'),
                BotCommand(command='media', description='Получить медиа-файлы'),
                BotCommand(command='local', description='Местоположение'),
                BotCommand(command='audio', description='Получить аудио'),
                BotCommand(command='sticker', description='Получить стикер')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

async def start():
    await menu_commands()

async def main():
    dp.include_router(rout_handlers)
    dp.startup.register(start)
    await bot.set_my_short_description('Тут я буду ебашить свой код')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')