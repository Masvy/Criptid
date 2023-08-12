from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.inline_start import language_kb, main_buttons_kb

start_router: Router = Router()


@start_router.message(CommandStart())
async def start(message: Message):
    '''Хэндлер для команды /start'''
    await message.answer(text='Выберите язык / Choose language',
                         reply_markup=language_kb)


@start_router.callback_query(F.data == 'russian_pressed')
async def show_main_menu(callback: CallbackQuery):
    await callback.message.edit_text(text=f'Здравствуйте, {callback.from_user.first_name}',
                                     reply_markup=main_buttons_kb)
