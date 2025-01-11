from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import dp, bot


# forward_message_callback_data = CallbackData('forward_message', 'text', 'message_id', 'chat_id', 'confirmation')


# Echo bot
@dp.message_handler(state=None)
async def forward_message_function(message: types.Message):
    forwarded_msg = await bot.forward_message(
        chat_id=2023386058,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )
    msg = await message.reply(text="📩 Maktubingiz adminga yuborildi\n"
                                   "✅ Tasdiqlangandan so'ng kanalga joylanadi")
    await bot.send_message(
        chat_id=2023386058,
        text="Tasdiqlaysizmi?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="✅ Confirm",
                        callback_data=f"confirm_{forwarded_msg.message_id}_{message.text}_{msg.message_id}_{msg.chat.id}"
                    ),
                    InlineKeyboardButton(
                        text="❌ Reject",
                        callback_data=f"reject_{forwarded_msg.message_id}_{message.text}_{msg.message_id}_{msg.chat.id}"
                    )
                ],
            ]
        )
    )

    await bot.forward_message(
        chat_id=775946529,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )
    # msg = await message.reply(text="📩 Maktubingiz adminga yuborildi\n"
    #                                "✅ Tasdiqlangandan so'ng kanalga joylanadi")
    await bot.send_message(
        chat_id=775946529,
        text="Tasdiqlaysizmi?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="✅ Confirm",
                        callback_data=f"confirm_{forwarded_msg.message_id}_{message.text}_{msg.message_id}_{msg.chat.id}"
                    ),
                    InlineKeyboardButton(
                        text="❌ Reject",
                        callback_data=f"reject_{forwarded_msg.message_id}_{message.text}_{msg.message_id}_{msg.chat.id}"
                    )
                ],
            ]
        )
    )


@dp.callback_query_handler(lambda call: call.data.startswith("confirm_") or call.data.startswith("reject_"))
async def forward_message_to_channel_or_reject(call: types.CallbackQuery, callback_data: dict):
    data = call.data.split("_")
    action = data[0]
    forward_message_id = int(data[1])
    text = data[2]
    msg_id = int(data[3])
    msg_chat_id = int(data[4])
    if action == "confirm":
        await bot.send_message(
            chat_id=-1002222338084,
            text=text,
        )
        # await bot.send_message(chat_id=-1002222338084, text=text)

        await call.message.edit_text(text="✅ Kanalga joylandi")
        await bot.edit_message_text(text="✅ Kanalga joylandi", chat_id=msg_chat_id, message_id=msg_id)
    else:
        await call.message.edit_text(text="❌ Rad etildi")
        await bot.edit_message_text(text="❌ Rad etildi", chat_id=msg_chat_id, message_id=msg_id)
