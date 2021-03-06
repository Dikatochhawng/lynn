from pyrogram import filters
from pyrogram.types import Message

from wbb import SUDOERS, app
from wbb.core.decorators.errors import capture_err
from wbb.utils.dbfunctions import (blacklist_chat, blacklisted_chats,
                                   whitelist_chat)

__MODULE__ = "Blacklist Chat"
__HELP__ = """
**HE MODULE HI CHU DEVS TAN BIK ANI E**.

Devs Users tan lo chuan a work ve lem lo a
Midang tan chuan tangkaina avang viau.

➤/blacklist_chat [chat id] - Chat Blacklist a add na.
➤/whitelist_chat [chat id] - Chat Whitelist a add na.
➤/blacklisted - blacklisted chat ho enna.
"""


@app.on_message(filters.command("blacklist_chat") & filters.user(SUDOERS))
@capture_err
async def blacklist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "**Usage:**\n/blacklist_chat [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await blacklisted_chats():
        return await message.reply_text("blacklist a a in add daih tawh.")
    blacklisted = await blacklist_chat(chat_id)
    if blacklisted:
        return await message.reply_text(
            "Hlawhtling takin blacklist add ani e"
        )
    await message.reply_text("Something wrong happened, check logs.")


@app.on_message(filters.command("whitelist_chat") & filters.user(SUDOERS))
@capture_err
async def whitelist_chat_func(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "**Usage:**\n/whitelist_chat [CHAT_ID]"
        )
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats():
        return await message.reply_text("Chat is already whitelisted.")
    whitelisted = await whitelist_chat(chat_id)
    if whitelisted:
        return await message.reply_text(
            "Hlawhtling takin whitelist add ani e"
        )
    await message.reply_text("Something wrong happened, check logs.")


@app.on_message(filters.command("blacklisted_chats") & filters.user(SUDOERS))
@capture_err
async def blacklisted_chats_func(_, message: Message):
    text = ""
    for count, chat_id in enumerate(await blacklisted_chats(), 1):
        try:
            title = (await app.get_chat(chat_id)).title
        except Exception:
            title = "Private"
        text += f"**{count}. {title}** [`{chat_id}`]\n"
    await message.reply_text(text)
