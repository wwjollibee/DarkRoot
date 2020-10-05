import re
from math import ceil
from userbot.plugins import inlinestats
from telethon import custom, events, Button
from userbot import ALIVE_NAME
from userbot import CMD_LIST

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DarkUserBot"
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("DarkUB"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "kömək")
            result = builder.article(
                "© Userbot Help",
                text="{}\nPluginlərin sayı: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        if query == "Vəziyyət":
           result = builder.article(
           title="Stats",
           text=f"**Statistikalar göstərilir: {DEFAULTUSER}**",
           buttons = [
                   [custom.Button.inline("Statların", data="terminator")],
                   [Button.url("Repomuz 🛡️", "http://github.com/DarkWebAze/DarkUserBot")],
             ]
         )
        await event.answer([result] if result else None)
    @tgbot.on(
        events.callbackquery.CallbackQuery( 
            data=re.compile(b"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "help")
            await event.edit(buttons=buttons)
        else:
            reply_popp_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(
            data=re.compile(b"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"
            )
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery( 
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            try:
                for i in CMD_LIST[plugin_name]:
                    help_string += i
                    help_string += "\n"
            except:
                pass
            if help_string is "":
                reply_pop_up_alert = "{} faydasızdır".format(plugin_name)
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Bu plugini silmək üçün .unload {} istifadə edin\n\
                © Userbot".format(
                plugin_name
            )
            try:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            except:
                halps = "Komutların siyahısını almaq üçün .help {} edin.".format(plugin_name)
                await event.answer(halps, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Zəhmət olmasa öz Userbotunu alın və məndən istifadə etməyin!"

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
    async def rip(event):
            if event.query.user_id == bot.uid:
                text = inlinestats
                await event.answer(text, alert=True)
            else:
                txt = "Sahibimin Statistikasına baxa bilməzsiniz"
                await event.answer(txt, alert=True)
                
def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 8
    number_of_cols = 2
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{} {} {}".format("✨", x, "✨"), data="us_plugin_{}".format(x)
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "Geri", data="{}_Geri({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "İrəli", data="{}_İrəli({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs
