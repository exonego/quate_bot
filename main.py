import asyncio
import logging

from aiogram import Bot, Dispatcher

from config.config import Config, load_config
from database.database import init_db
from keyboards.menu_commands import set_main_menu
from handlers.other import other_router
from handlers.user import user_router

# init logger
logger = logging.getLogger(__name__)


# function config and launch bot
async def main():
    # load config
    config: Config = load_config()

    # set basic logging config
    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format,
        style=config.log.style,
    )

    logger.info("Starting bot")

    # init bot and dispatcher
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    # init "database"
    db: dict = init_db()

    # save "database" into workflow_data
    dp.workflow_data.update(db=db)

    # setting bot-commands main menu
    await set_main_menu(bot)

    # register routers into dispatcher
    dp.include_router(user_router)
    dp.include_router(other_router)

    # skip updates and run polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
