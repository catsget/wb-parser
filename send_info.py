from aiogram import Bot
from parse_json import parse_wb_sync


async def send_info(bot: Bot, user_id: int, article: int):
    try:
        data = parse_wb_sync(nm=article)

        if (data and len(data["products"]) > 0 and "price" in data["products"][0]["sizes"][0]):
            brand = data["products"][0]["brand"]
            name = data["products"][0]["name"]
            supplier = data["products"][0]["supplier"]
            basic_price = int(data["products"][0]["sizes"][0]["price"]["basic"] / 100)
            price_with_discount = int(
                data["products"][0]["sizes"][0]["price"]["product"] / 100
            )

            await bot.send_message(
                user_id,
                f"Бренд {brand}\nПоставщик {supplier}\n\n{name}\n\nОбычная цена: {basic_price} рублей\nЦена со скидкой: {price_with_discount} рублей",
            )
    except Exception:
        print("Неправильный айди пользователя или артикуль")
