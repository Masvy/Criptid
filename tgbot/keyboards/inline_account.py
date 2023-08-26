from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Объект клавиатуру, в котором находятся объекты кнопок
account_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Привязать карту 💳',
                              callback_data='link_card_pressed')],
        [InlineKeyboardButton(text='Меню📋',
                              callback_data='menu_pressed')]
    ]
)
