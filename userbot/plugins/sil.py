# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for purging unneeded messages(usually spam or ot). """

from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.utils import errors_handler, register


@register(outgoing=True, pattern="^.sil$")
@errors_handler
async def fastpurger(purg):
    """ Kod: .sil, göstərdiyiniz mesajdan aşağı bütün mesajları silir. """
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "`Təmizlik Bitti!\n`Silindi " + str(count) + " mesaj.",
    )

    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID, str(count) + " mesaj uğurla silindi."
        )
    await sleep(2)
    await done.delete()


@register(outgoing=True, pattern="^.silm")
@errors_handler
async def purgeme(delme):
    """ Kod: .silm, sənin x sayda mesajını silir."""
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Təmizlik Bitti!` Təmizləndi " + str(count) + " mesaj.",
    )
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID, str(count) + " mesaj uğurla silindi."
        )
    await sleep(2)
    i = 1
    await smsg.delete()


@register(outgoing=True, pattern="^.s$")
@errors_handler
async def delete_it(delme):
    """ Kod: .s, sadəcə göstərdiyiniz mesajı silir. """
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Mesaj Uğurla Silindi!"
                )
        except rpcbaseerrors.BadRequestError:
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "Yaxşı, mesajları silə bilmirəm"
                )


@register(outgoing=True, pattern="^.edit")
@errors_handler
async def editer(edit):
    """ For .editme command, edit your last message. """
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id("me")
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if BOTLOG:
        await edit.client.send_message(
            BOTLOG_CHATID, "Edit query was executed successfully"
        )


@register(outgoing=True, pattern="^.sd")
@errors_handler
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID, "sd query done successfully")


CMD_HELP.update(
    {
        "Sil": ".sil\
        \nİstifadəsi: Göstərdiyiniz mesajdan aşağıdakı bütün mesajları silir."
    }
)

CMD_HELP.update(
    {
        "Silm": ".silm <x>\
        \nİstifadəsi: Sənin x sayda mesajını silir."
    }
)

CMD_HELP.update(
    {
        "S": ".s\
\nİstifadəsi: Sadəcə göstərdiyiniz mesajı silir."
    }
)

CMD_HELP.update(
    {
        "edit": ".edit <newmessage>\
\nUsage: Replace your last message with <newmessage>."
    }
)

CMD_HELP.update(
    {
        "sd": ".sd <x> <message>\
\nUsage: Creates a message that selfdestructs in x seconds.\
\nKeep the seconds under 100 since it puts your bot to sleep."
    }
)
