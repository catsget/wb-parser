from aiogram import Router, types
from to_int import to_int
from parse_json import parse_wb_sync
from send_info import send_info
import handlers

router = Router()

@router.message()
async def article_handler(message: types.Message):
    bot = handlers.main_bot

    user_id = message.from_user.id
    article = to_int(message.text)

    if isinstance(article, int) and len(message.text) == 9:
        data = parse_wb_sync(nm=article)
        
        if data and len(data["products"]) > 0 and "price" in data["products"][0]["sizes"][0]:
            await send_info(bot, user_id, article)
            pass
        else:
            await message.answer("Артикул не валидный")
