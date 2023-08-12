from aiogram import Router, F
from aiogram.types import CallbackQuery

crypto_router: Router = Router()


@crypto_router.callback_query(F.data == 'cryptocurrencies_pressed')
async def show_cryptocurrencies(callback: CallbackQuery):
    await callback.message.edit_text(text='Спиок криптовалют, возможных для '
                                     'обмена в нашем сервисе. Выберите ту, '
                                     'которую хотите обменять:')
