import asyncio
import logging
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from database import init_db
from handlers import register_routes
from monitoring import monitoring

load_dotenv()
BOT_TOKEN = getenv("BOT_TOKEN")

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=storage)


async def main():
    await init_db()

    register_routes(dp, bot)

    asyncio.create_task(monitoring(bot))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
