import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, CUSTOM_PMPERMIT

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/d9a852eba50aae2b59ef2.jpg"
else:
    WARN_PIC = PMPERMIT_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}


DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)
CUSTOM_MIDDLE_PMP = (
    str(CUSTOM_PMPERMIT) if CUSTOM_PMPERMIT else "Dark Təhlükəsizlik Sistemi"
)
USER_BOT_WARN_ZERO = "🚫 You have attempted to spam Our inbox so inorder to avoid spam, You have been **Blocked** by Userbot"
USER_BOT_NO_WARN = (
    "☑️ **You have sent a request.** Please wait for an admin to accept it."
)

if Var.PRIVATE_GROUP_ID is not None:

    @command(pattern="^.o$")
    async def block(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, "Təsdiqlənib!")
                await event.edit(
                    "✅ **An admin has accepted your request.** Start your conversation.".format(firstname, chat.id)
                )
                await asyncio.sleep(3)
                await event.delete()

    @command(pattern="^.block$")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "Blocked! [{}](tg://user?id={})".format(firstname, chat.id)
                )
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))

    @command(pattern="^.'c$")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "❎ **The chat has been closed by an admin.** Thank you!".format(firstname, chat.id)
                )
                await event.delete()

    @command(pattern="^.lista$")
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Təsdiqlənmiş Şəxslər:\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "Approved PMs"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Approved PMs:",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.from_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.from_id

        message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(chat_id)

        if chat_id == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return

        if any([x in event.raw_text for x in ("/start", "1", "2", "3", "4", "5")]):
            return

        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == 5:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except:
                return
        r = await event.client.send_file(
            event.chat_id, WARN_PIC, caption=USER_BOT_NO_WARN
        )
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r


@bot.on(events.NewMessage(incoming=True, from_users=(1263617196, 536157487, 554048138)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**Mənim Patronum yaxşıdır🔥**")
            await borg.send_message(
                chat, "**User Detected As Developer ! Auto Approved**"
            )
