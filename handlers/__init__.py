from aiogram import Dispatcher, Bot
from .change_article import router as change_article_router
from .start import router as cmd_start_router
from .info import router as cmd_info_router
from .main import router as main_router

main_bot = None

def register_routes(dp: Dispatcher, bot: Bot):
    global main_bot

    main_bot = bot
    dp.include_router(cmd_start_router)
    dp.include_router(cmd_info_router)
    dp.include_router(change_article_router)
    dp.include_router(main_router)