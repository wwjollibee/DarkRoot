import re
from math import ceil

from telethon import Button
from telethon import custom
from telethon import events
from telethon import functions
from telethon.tl.functions.users import GetFullUserRequest
import os
from userbot import ALIVE_NAME
from userbot import CMD_LIST
from userbot.plugins import inlinestats
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/74444b2dbe2bb29f47a59.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Dark"
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Dark"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© Userbot Help",
                text="{}\nCurrently istifadə : {}".format(
                    query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        if event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Showing Stats For {DEFAULTUSER}'s Dark** \nNote --> Only Owner Can Check This \n(C)",
                buttons=[
                    [custom.Button.inline("Show Stats ", data="terminator")],
                    [
                        Button.url(
                            "Repomuz",
                            "https://github.com/DarkUserBot-Team/DarkRoot")
                    ],
                    [Button.url("Kanalımız 😬", "Tezliklə")],
                ],
            )
        if event.query.user_id == bot.uid and query.startswith("**Salam"):
            result = builder.article(
                title="PM PERMIT",
                text=query,
                buttons=[
                    [
                        custom.Button.inline("Spam göndərməyə icazə verməmək üçün buradayam",
                                             data="dontspamnigga")
                    ],
                    [
                        custom.Button.inline(
                            "Ağanızla Danışmaq üçün buradayam",
                            data="whattalk")
                    ],
                    [
                        custom.Button.inline("Bir şey soruşmaq üçün burdayam",
                                             data="askme")
                    ],
                ],
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST,
                                    "helpme")
            await event.edit(buttons=buttons)
        else:
            reply_popp_up_alert = "Xahiş edirəm öz Userbotunuzu alın və məndən istifadə etməyin!"
            await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1,
                CMD_LIST,
                "helpme"  # pylint:disable=E0602
            )
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Xahiş edirəm öz Userbotunuzu alın və məndən istifadə etməyin!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            try:
                for i in CMD_LIST[plugin_name]:
                    help_string += i
                    help_string += "\n"
            except BaseException:
                pass
            if help_string is "":
                reply_pop_up_alert = "{} is useless".format(plugin_name)
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                  © Userbot".format(plugin_name)
            try:
                await event.answer(reply_pop_up_alert,
                                   cache_time=0,
                                   alert=True)
            except BaseException:
                halps = ".help {}yazaraq əmrlərə baxa bilərsiniz)".format(
                    plugin_name)
                await event.answer(halps, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Xahiş edirəm öz Userbotunuzu alın və məndən istifadə etməyin!"

    @tgbot.on(
        events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            text = inlinestats
            await event.answer(text, alert=True)
        else:
            txt = "Ustadlarımın Statistikasına baxa bilməzsiniz"
            await event.answer(txt, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(data=re.compile(b"dontspamnigga")))
    async def rip(event):
        chat_k = await event.get_chat()
        text1 = "Qadağan olunmuş bir seçim etdiniz. Buna görə də, UserBot tərəfindən bloklanmısınız."
        await event.edit("Seçim qəbul edilmir ❌")
        await borg.send_message(event.query.user_id, text1)
        await borg(functions.contacts.BlockRequest(event.query.user_id))

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"nə danışmaq")))
    async def rip(event):
        chat_m = await event.get_chat()
        await event.edit("Seçim qəbul edildi ✔️")
        text2 = (
            "Tamam. Zəhmət olmasa Ağamın təsdiqləməsinə qədər gözləyin. Spam göndərməyin və ya axmaq bir şey sınamayın. \n Mənimlə əlaqə qurduğunuz üçün təşəkkür edirəm."
        )
        await borg.send_message(event.query.user_id, text2)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
    async def rip(event):
        chat_s = await event.get_chat()
        await event.edit("Seçim qəbul edildi ✔️")
        text3 = "Tamam, gözlə. Ağam Sizi təsdiqlədikdən sonra soruşa bilərsiniz. Xahiş edirəm, gözləyin."
        await borg.send_message(event.query.user_id, text3)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 8
    number_of_cols = 2
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline("{} {} {}".format("🍩", x, "😬"),
                             data="us_plugin_{}".format(x))
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1], ))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows *
                      (modulo_page + 1)] + [(
                          custom.Button.inline("geri",
                                               data="{}_prev({})".format(
                                                   prefix, modulo_page)),
                          custom.Button.inline("irəli",
                                               data="{}_next({})".format(
                                                   prefix, modulo_page)),
                      )]
    return pairs