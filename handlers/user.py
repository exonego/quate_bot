from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from keyboards.favorites_kb import create_favorites_keyboard, create_edit_keyboard
from keyboards.quates_kb import quate_kb
from services.services import choice_quate
from lexicon.lexicon import LEXICON_RU

user_router = Router()


# this handler will react to command "/start"
@user_router.message(CommandStart())
async def process_start_command(message: Message, db: dict):
    await message.answer(LEXICON_RU[message.text])
    if message.from_user.id not in db["users"]:
        db["users"][message.from_user.id] = deepcopy(db.get("user_template"))


# this handler will react to command "/help"
@user_router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU[message.text])


# this handler will react to command "/quate"
@user_router.message(Command(commands="quate"))
async def process_quate_command(message: Message, db: dict, quates: dict):
    quate_num = choice_quate(quates)
    db["users"][message.from_user.id]["cur_quate"] = quate_num
    await message.answer(text=quates[quate_num], reply_markup=quate_kb)


# this handler will react to command "/favorites"
@user_router.message(Command(commands="favorites"))
async def process_favorites_command(message: Message, db: dict, quates: dict):
    if db["users"][message.from_user.id]["favorites"]:
        await message.answer(
            text=LEXICON_RU[message.text],
            reply_markup=create_favorites_keyboard(
                quates, *sorted(db["users"][message.from_user.id]["favorites"])
            ),
        )
    else:
        await message.answer(text=LEXICON_RU["no_favorites"])


@user_router.callback_query(F.data == "kb_quate_like")
async def process_quate_like(callback: CallbackQuery, db: dict):
    db["users"][callback.from_user.id]["favorites"].add(
        db["users"][callback.from_user.id]["cur_quate"]
    )
    await callback.answer("Цитата добавлена в избранные!")


@user_router.callback_query(F.data == "kb_quate_send")
async def process_quate_send(callback: CallbackQuery, db: dict, quates: dict):
    quate_num = choice_quate(quates)
    db["users"][callback.from_user.id]["cur_quate"] = quate_num
    await callback.message.edit_text(text=quates[quate_num], reply_markup=quate_kb)
    await callback.answer("Новая цитата!")
