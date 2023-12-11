import asyncio, logging, sys, json
from aiogram import Bot, Dispatcher
from aiogram.types import FSInputFile

from handlers import commands, messages, games, state, admin



with open("db/config.json", 'r', encoding='utf-8') as json_file:
    config = json.load(json_file)




bot = Bot(config["TOKEN"], parse_mode='HTML')
async def main():
    dp = Dispatcher()
    dp.include_routers(commands.router, games.router, state.router, admin.router, messages.router)
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)

if __name__ == '__main__':
    asyncio.run(main())