from aiogram import types, filters, Router
from database.users import get_or_create_user

router = Router()

change_article = types.KeyboardButton(text="Поменять артикул")

main_keyboard = types.ReplyKeyboardMarkup(
    resize_keyboard=True, keyboard=[[change_article]]
)


@router.message(filters.CommandStart())
async def cmd_start(message: types.Message):
    user_id = message.from_user.id

    await get_or_create_user(user_id)

    await message.answer("Привет! Отправь мне артикул WB", reply_markup=main_keyboard)
