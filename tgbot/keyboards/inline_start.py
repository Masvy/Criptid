from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Объект клавиатуру, в котором находятся объекты кнопок
language_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Русский 🇷🇺',
                                 callback_data='russian_pressed'),
            InlineKeyboardButton(text='English 🇬🇧',
                                 callback_data='english_pressed')
        ]
    ]
)

# Объект клавиатуру, в котором находятся объекты кнопок
main_buttons_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Аккаунт 🪪',
                                 callback_data='account_pressed'),
            InlineKeyboardButton(text='Криптовалюты 🪙',
                                 callback_data='cryptocurrencies_pressed')
        ],
        [
            InlineKeyboardButton(text='История обмена 🗃️',
                                 callback_data='history_pressed'),
            InlineKeyboardButton(text='Резервы сервиса 💰',
                                 callback_data='reserves_pressed')
        ],
        [InlineKeyboardButton(text='Прогноз от Chat GPT 📈',
                              callback_data='forecast_pressed')],
        [
            InlineKeyboardButton(text='Контакты 📱',
                                 callback_data='contacts_pressed'),
            InlineKeyboardButton(text='Отзывы 📢',
                                 callback_data='reviews_pressed')
        ]
    ]
)
