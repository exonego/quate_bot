from aiogram import Router
from aiogram.types import Message

from lexicon.lexicon import LEXICON_RU

other_router = Router()


# this handler will react to any incorrect messages
@other_router.message()
async def process_incorrect(message: Message):
    await message.answer(text=LEXICON_RU["incorrect"])
