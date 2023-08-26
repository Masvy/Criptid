from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_other import contacts_kb, reviews_kb

other_router: Router = Router()


@other_router.callback_query(F.data == 'contacts_pressed')
async def show_contacts(callback: CallbackQuery):
    '''Хендлер реагирует на кнопку: Контакты 📱'''
    await callback.message.edit_text(text='Наша контактная информация:',
                                     reply_markup=contacts_kb)


@other_router.callback_query(F.data == 'reviews_pressed')
async def show_reviews(callback: CallbackQuery):
    '''Хендлер реагирует на кнопку: Отзывы 📢'''
    await callback.message.edit_text(text='Отзывы на наш сервис:',
                                     reply_markup=reviews_kb)
