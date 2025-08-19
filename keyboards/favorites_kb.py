from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


def create_favorites_keyboard(*args: str) -> InlineKeyboardMarkup:
    # create kb builder
    kb_builder = InlineKeyboardBuilder()
    # fill the keyboard with quate-buttons
    for button in sorted(args):
        kb_builder.row(InlineKeyboardButton(text=button, callback_data=button))
    # add into keyboard edit and cancel buttons
    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON_RU["edit_favorites_button"], callback_data="edit_favorites"
        ),
        InlineKeyboardButton(text=LEXICON_RU["cancel"], callback_data="cancel"),
        width=2,
    )
    return kb_builder.as_markup()


def create_edit_keyboard(*args: str) -> InlineKeyboardMarkup:
    # create kb builder
    kb_builder = InlineKeyboardBuilder()
    # fill the keyboard with quate-buttons
    for button in sorted(args):
        kb_builder.row(
            InlineKeyboardButton(
                text=f"{LEXICON_RU["del"]} {button}", callback_data=f"{button}del"
            )
        )
    # add into keyboard cancel button
    kb_builder.row(
        InlineKeyboardButton(text=LEXICON_RU["cancel"], callback_data="cancel")
    )
    return kb_builder.as_markup()
