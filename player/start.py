from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import SOURCE_CODE, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME
from plugins.tr import *
from plugins.tr import TGPK_TEXT, VSONG_TEXT, PASTE_TEXT, INFO_TEXT, STREAM_TEXT, START_TEXT, HELP_TEXT
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("❔ Helps❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("Source", url=f"https://github.com/King-Amda"),
                InlineKeyboardButton("Group", url=f"https://t.me/songandquiz"),
            ],
            [
                InlineKeyboardButton("Owner", url=f"https://t.me/NiupunDinujaya"),
                InlineKeyboardButton("Assistant", url=f"https://t.me/chathush99"),
            ],
            [
               InlineKeyboardButton("💞 Add Me 💞", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
      m=await message.reply_photo(
                                  photo="https://telegra.ph/file/1ca2830c014aa6b8b62e7.jpg", 
                                  caption=START_TEXT.format(message.from_user.first_name, message.from_user.id),
                                  reply_markup=reply_markup
      )      
   else:
      await message.reply(f"**👋 Hey Nipun Music Player is Alive! ✨**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("Sᴛʀᴇᴀᴍ", callback_data="stream"),
                InlineKeyboardButton ("Iɴꜰᴏ Wʜᴏɪꜱ", callback_data="info"),
            ],
            [
                InlineKeyboardButton("Vɪᴅᴇᴏ Sᴏɴɢ", callback_data="vsong"),
                InlineKeyboardButton ("Pᴀꜱᴛᴇ", callback_data="paste"),
            ],
            [
               InlineKeyboardButton("Tᴇʟᴇ ✮ ɢʀᴀᴘʜ", callback_data="tgph"),
            ],
            [
               InlineKeyboardButton("Owner", url=f"https://t.me/NiupunDinujaya"),
               InlineKeyboardButton("Back", callback_data="start"),
               InlineKeyboardButton ("Assistant", url=f"https://t.me/chathush99"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="tgph":
        buttons = [
            [
                InlineKeyboardButton ("Back", callback_data="help"),
                InlineKeyboardButton("Owner", url=f"https://t.me/NiupunDinujaya"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                TGPK_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="stream":
        buttons = [
            [
                InlineKeyboardButton ("Back", callback_data="help"),
                InlineKeyboardButton("Owner", url=f"https://t.me/NiupunDinujaya"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                STREAM_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="paste":
        buttons = [
            [
                InlineKeyboardButton ("Back", callback_data="help"),
                InlineKeyboardButton("Owner", url=f"https://t.me/NiupunDinujaya"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                PASTE_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="vsong":
        buttons = [
            [
                InlineKeyboardButton ("Back", callback_data="help"),
                InlineKeyboardButton("Owner", url=f"https://t.me/NipunDinujayaOffline"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                VSONG_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="info":
        buttons = [
            [
                InlineKeyboardButton ("Back", callback_data="help"),
                InlineKeyboardButton("Owner", url=f"https://t.me/NiupunDinujaya"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                INFO_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("❔ Help❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("Source", url=f"https://github.com/King-Amda"),
                InlineKeyboardButton("Group", url=f"https://t.me/songandquiz"),
            ],
            [
                InlineKeyboardButton("Owner", url=f"https://t.me/NipunDinujayaOffline"),
                InlineKeyboardButton("Assistant", url=f"https://t.me/chathush99"),
            ],
            [
               InlineKeyboardButton("💞 Add Me 💞", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
