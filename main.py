from aiogram import Dispatcher, Bot
import asyncio, start_handler

bot=Bot("8292650868:AAGo3Sm4Hrraz2vf0rlHFdoLwkHyFdxHpOM")
dp=Dispatcher()

dp.include_router(start_handler.router)


async def main():
    print("Bot started!")
    await dp.start_polling(bot)


asyncio.run(main())




