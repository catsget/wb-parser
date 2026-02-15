import asyncio
import logging
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.users import get_all_users
from send_info import send_info

logging.getLogger("apscheduler").setLevel(logging.ERROR)


async def check_all_articles(bot: Bot):
    users = await get_all_users()

    for user in users:
        user_id = user["user_id"]
        article = user["article"]

        await send_info(bot, user_id, article)
        await asyncio.sleep(0.5)


async def monitoring(bot: Bot):
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        check_all_articles, "interval", minutes=60, args=[bot]
    )

    scheduler.start()

    try:
        while True:
            await asyncio.sleep(60)
    except Exception as e:
        print(e)
