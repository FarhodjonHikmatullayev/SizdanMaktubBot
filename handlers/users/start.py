from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot


@dp.callback_query_handler(text="check", state="*")
async def bot_start(call: types.CallbackQuery, state: FSMContext):
    try:
        await state.finish()
    except:
        pass
    user_telegram_id = call.from_user.id
    users = await db.select_users(telegram_id=user_telegram_id)
    if not users:
        full_name = call.from_user.full_name
        username = call.from_user.username
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=user_telegram_id
        )
        role = user['role']
    else:
        user = users[0]
        role = user['role']

    if role == 'user':
        await call.message.answer(text="👋 Salom, xush kelibsiz!\n"
                                       "✉️ Yo'llamoqchi bo'lgan maktubingizni yozing:")
    else:
        await call.message.answer(text="👋 Salom, xush kelibsiz!\n"
                                       "✉️ Yo'llamoqchi bo'lgan maktubingizni yozing:")


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    try:
        await state.finish()
    except:
        pass
    user_telegram_id = message.from_user.id
    users = await db.select_users(telegram_id=user_telegram_id)
    if not users:
        full_name = message.from_user.full_name
        username = message.from_user.username
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=user_telegram_id
        )
        role = user['role']
    else:
        user = users[0]
        role = user['role']

    if role == 'user':
        await message.answer(text="👋 Salom, xush kelibsiz!\n"
                                  "✉️ Yo'llamoqchi bo'lgan maktubingizni yozing:")
    else:
        await message.answer(text="👋 Salom, xush kelibsiz!\n"
                                  "✉️ Yo'llamoqchi bo'lgan maktubingizni yozing:")
