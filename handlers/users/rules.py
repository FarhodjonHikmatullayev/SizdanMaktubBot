from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db


@dp.message_handler(commands=['qoidalar'], state="*")
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
        await message.answer(text="📝 *“Sizdan Maktublar” botining qoidalari:*  \n"
                                  "1. Siz faqat qisqa matn (fikr, she’r, yoki kichik hikoya) yuborishingiz mumkin.  \n"
                                  "2. Linklar, reklama, telefon raqamlari yoki nomaqbul so‘zlar taqiqlangan.  \n"
                                  "3. Bir kunda maksimal 5 ta matn yuborishingiz mumkin.\n"
                                  "4. Har bir yuborilgan matn avtomatik tarzda tekshiriladi.  \n\n"
                                  "Qoidalarga rioya qilganingiz uchun rahmat! 😊")
    else:
        await message.answer(text="📝 *“Sizdan Maktublar” botining qoidalari:*  \n"
                                  "1. Siz faqat qisqa matn (fikr, she’r, yoki kichik hikoya) yuborishingiz mumkin.  \n"
                                  "2. Linklar, reklama, telefon raqamlari yoki nomaqbul so‘zlar taqiqlangan.  \n"
                                  "3. Bir kunda maksimal 5 ta matn yuborishingiz mumkin.\n"
                                  "4. Har bir yuborilgan matn avtomatik tarzda tekshiriladi.  \n\n"
                                  "Qoidalarga rioya qilganingiz uchun rahmat! 😊")
