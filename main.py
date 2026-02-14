import asyncio
import logging
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from parse_json import parse_wb_sync
from to_int import to_int
from database import init_db
from database.users import get_article, update_article

load_dotenv()
BOT_TOKEN = getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Отправь мне артикул WB")


@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.answer(
        "Этот бот выводит всю информацию о ценах выбранного товара.\nВ скором времени появится мониторинг цен, он еще в разработке."
    )


@dp.message()
async def handle_article(message: types.Message):
    article = to_int(message.text)

    if isinstance(article, int) and len(message.text) == 9:
        data = parse_wb_sync(nm=article)
        if data and len(data["products"]) > 0:
            brand = data["products"][0]["brand"]
            name = data["products"][0]["name"]
            supplier = data["products"][0]["supplier"]
            basic_price = int(data["products"][0]["sizes"][0]["price"]["basic"] / 100)
            price_with_discount = int(
                data["products"][0]["sizes"][0]["price"]["product"] / 100
            )

            await message.answer(
                f"Бренд {brand}\nПоставщик {supplier}\n\n{name}\n\nОбычная цена: {basic_price} рублей\nЦена со скидкой: {price_with_discount} рублей"
            )
        else:
            await message.answer("Артикул не валидный")


async def main():
    await init_db()

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
