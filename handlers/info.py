from aiogram import types, filters, Router
from database.users import get_or_create_user

router = Router()


@router.message(filters.Command("info"))
async def cmd_info(message: types.Message):
    await message.answer(
        "Этот бот выводит всю информацию о ценах выбранного товара.\nВ скором времени появится мониторинг цен, он еще в разработке."
    )
