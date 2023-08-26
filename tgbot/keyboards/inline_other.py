from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Объект клавиатуру, в котором находятся объекты кнопок
contacts_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сайт 🌐',
                                 callback_data='website_pressed'),
            InlineKeyboardButton(text='Эл. Почта 📧',
                                 callback_data='email_pressed')
        ],
        [InlineKeyboardButton(text='Меню 📋',
                              callback_data='menu_pressed')]
    ]
)

reviews_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Bestchange',
                              url='https://www.bestchange.ru/list.html')],
        [InlineKeyboardButton(text='Okchanger',
                              url='https://www.okchanger.ru/exchangers')],
        [InlineKeyboardButton(text='Меню 📋',
                              callback_data='menu_pressed')]
    ]
)
