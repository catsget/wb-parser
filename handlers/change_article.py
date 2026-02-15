from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from to_int import to_int
from database.users import update_article
from handlers.start import cmd_start

router = Router()

class ArticleStates(StatesGroup):
    change_state = State()

@router.message(F.text == "Поменять артикул")
async def change_article_handler(message: types.Message, state: FSMContext):
    await message.answer("testtttttt")
    await state.set_state(ArticleStates.change_state)

@router.message(ArticleStates.change_state)
async def change_article(message: types.Message, state: FSMContext):
    article = to_int(message.text)
    user_id = message.from_user.id

    if isinstance(article, int) and len(str(article)) == 9:
        await update_article(user_id, article)
        await message.answer("Артикуль изменен")
        await state.clear()
        await cmd_start(message)