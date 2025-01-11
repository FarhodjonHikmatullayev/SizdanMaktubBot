from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import dp, bot

forward_message_callback_data = CallbackData('forward_message', 'text', 'message_id', 'chat_id', 'confirmation')


# Echo bot
@dp.message_handler(state=None)
async def forward_message_function(message: types.Message):
    await bot.forward_message(
        chat_id=775946529,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )
    msg = await message.reply(text="📩 Maktubingiz adminga yuborildi\n"
                                   "✅ Tasdiqlangandan so'ng kanalga joylanadi")
    await bot.send_message(
        chat_id=775946529,
        text="Tasdiqlaysizmi?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="✅ Confirm",
                        callback_data=forward_message_callback_data.new(
                            text=message.text,
                            message_id=msg.message_id,
                            chat_id=msg.chat.id,
                            confirmation="confirm"
                        )
                    ),
                    InlineKeyboardButton(
                        text="❌ Reject",
                        callback_data=forward_message_callback_data.new(
                            text=message.text,
                            message_id=msg.message_id,
                            chat_id=msg.chat.id,
                            confirmation="reject"
                        )
                    )
                ],
            ]
        )
    )


@dp.callback_query_handler(forward_message_callback_data.filter())
async def forward_message_to_channel_or_reject(call: types.CallbackQuery, callback_data: dict):
    text = callback_data.get('text')
    message_id = int(callback_data.get('message_id'))
    chat_id = int(callback_data.get('chat_id'))
    confirmation = callback_data.get('confirmation')
    if confirmation == "confirm":
        await bot.send_message(
            chat_id=-1002222338084,
            text=text,
        )

        await call.message.edit_text(text="✅ Kanalga joylandi")
        await bot.edit_message_text(text="✅ Kanalga joylandi", chat_id=chat_id, message_id=message_id)
    else:
        await call.message.edit_text(text="❌ Rad etildi")
        await bot.edit_message_text(text="❌ Rad etildi", chat_id=chat_id, message_id=message_id)
