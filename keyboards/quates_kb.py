from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicon.lexicon import LEXICON_RU


quate_kb = InlineKeyboardMarkup(
    *[
        [
            InlineKeyboardButton(
                text=LEXICON_RU["kb_quate_like"], callback_data="kb_quote_like"
            ),
            InlineKeyboardButton(
                text=LEXICON_RU["kb_quate_send"], callback_data="kb_quate_send"
            ),
        ]
    ]
)
