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
        await call.message.answer(text="👋Assalomu alaykum! 😊\n"
                                       "Siz “Sizdan Maktublar” botiga xush kelibsiz!")
        await call.message.answer(text="Iltimos, qoidalar bilan tanishib chiqing:  \n"
                                       "1. Faqat matn yuborishingiz mumkin.\n"
                                       "2. Reklama, linklar va haqoratli so‘zlar taqiqlangan.\n"
                                       "3. Matningiz 300 belgidan oshmasligi kerak.\n\n"
                                       "Boshlash uchun matn yuboring!")
    else:
        await call.message.answer(text="👋Assalomu alaykum! 😊\n"
                                       "Siz “Sizdan Maktublar” botiga xush kelibsiz!")
        await call.message.answer(text="Iltimos, qoidalar bilan tanishib chiqing:  \n"
                                       "1. Faqat matn yuborishingiz mumkin.\n"
                                       "2. Reklama, linklar va haqoratli so‘zlar taqiqlangan.\n"
                                       "3. Matningiz 300 belgidan oshmasligi kerak.\n\n"
                                       "Boshlash uchun matn yuboring!")


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
        await message.answer(text="👋Assalomu alaykum! 😊\n"
                                  "Siz “Sizdan Maktublar” botiga xush kelibsiz!")
        await message.answer(text="Iltimos, qoidalar bilan tanishib chiqing:  \n"
                                  "1. Faqat matn yuborishingiz mumkin.\n"
                                  "2. Reklama, linklar va haqoratli so‘zlar taqiqlangan.\n"
                                  "3. Matningiz 300 belgidan oshmasligi kerak.\n\n"
                                  "Boshlash uchun matn yuboring!")
    else:
        await message.answer(text="👋Assalomu alaykum! 😊\n"
                                  "Siz “Sizdan Maktublar” botiga xush kelibsiz!")
        await message.answer(text="Iltimos, qoidalar bilan tanishib chiqing:  \n"
                                  "1. Faqat matn yuborishingiz mumkin.\n"
                                  "2. Reklama, linklar va haqoratli so‘zlar taqiqlangan.\n"
                                  "3. Matningiz 300 belgidan oshmasligi kerak.\n\n"
                                  "Boshlash uchun matn yuboring!")
