import logging
from datetime import datetime, timedelta

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.misc import subscription
from loader import bot, db


class CheckSubscriptionMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            chat_type = 'message'
            chat_id = update.message.chat.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
            chat_type = 'callback'
            chat_id = update.callback_query.message.chat.id
        else:
            # Foydalanuvchi ID aniqlanmagan holatda, xato yuz bermasligi uchun qaytarib yuborish
            raise CancelHandler()

        result = f"✨ Assalomu alaykum! 🎉\n" \
                 f"📩 Maktub yo'llash uchun sahifalarimizga obuna bo‘ling"
        final_status = True
        channels = await db.select_all_channels()
        inline_keyboard = InlineKeyboardMarkup(row_width=1)

        for channel in channels:
            chat_id_channel = int(channel['chat_id'])
            status = await subscription.check(user_id=user, channel=chat_id_channel)
            final_status *= status
            channel_info = await bot.get_chat(chat_id_channel)

            if not status:
                invite_link = await channel_info.export_invite_link()
                button = InlineKeyboardButton(text=channel_info.title, url=invite_link)
                inline_keyboard.add(button)

        button = InlineKeyboardButton(text="Obunani tekshirish", callback_data='check')
        inline_keyboard.add(button)

        if not final_status:
            if chat_type == 'message':
                await update.message.answer(result, reply_markup=inline_keyboard, disable_web_page_preview=True)
            elif chat_type == 'callback':
                # await update.callback_query.message.answer(result, reply_markup=inline_keyboard,
                #                                            disable_web_page_preview=True)
                await bot.edit_message_reply_markup(chat_id=chat_id,
                                                    message_id=update.callback_query.message.message_id,
                                                    reply_markup=inline_keyboard)
                await update.callback_query.answer()  # Callback so'rovini tasdiqlash
            raise CancelHandler()
        # if chat_type == 'callback':
        #     await bot.edit_message_reply_markup(chat_id, update.callback_query.message.message_id, reply_markup=None)
