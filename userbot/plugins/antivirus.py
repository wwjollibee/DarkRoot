# Lots of lub to @r4v4n4 for gibing the base <3
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import admin_cmd


@borg.on(admin_cmd("scan ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```İstənilən istifadəçi mesajına cavab verin.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```bir media mesajına cavabe```")
        return
    chat = "@DrWebBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```İstifadəçilər mesajına cavab verin.```")
        return
    await event.edit(" `İstifadəçilər mesajına cavab verin`")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=161163358)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Zəhmət olmasa @sangmatainfo_bot'u blokdan çıxarın və yenidən cəhd edin```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "```irəliləyən gizlilik ayarlarınızı söndürə bilərsinizmi?```"
            )
        else:
            if response.text.startswith("Seçin"):
                await event.edit("`Zəhmət olmasa` @DrWebBot`-a daxil olun və dilinizi seçin.`")
            else:
                await event.edit(
                    f"**Antivirus xidməti tamamlandı. Mənim son nəticələrim var.**\n {response.message.message}"
                )
