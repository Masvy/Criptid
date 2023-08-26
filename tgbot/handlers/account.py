from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_account import account_kb

account_router: Router = Router()


@account_router.callback_query(F.data == 'account_pressed')
async def show_account(callback: CallbackQuery):
    await callback.message.edit_text(text=f'Имя: {callback.from_user.first_name}\n'
                                     'Количество криптовалют: 0\n'
                                     'Всего произведено операций: 0\n'
                                     'Кошелёк:',
                                     reply_markup=account_kb)


@account_router.callback_query(F.data == 'link_card_pressed')
async def link_card(callback: CallbackQuery):
    await callback.message.edit_text(text='Ваша карта привязана.')
