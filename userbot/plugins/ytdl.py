# Thanks to @AvinashReddy3108 for this plugin

"""
Audio and video downloader using Youtube-dl
.yta To Download in mp3 format
.ytv To Download in mp4 format
"""

import asyncio
import math
import os
import time

from telethon.tl.types import DocumentAttributeAudio
from uniborg.util import admin_cmd, edit_or_reply, sudo_cmd
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)


async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Yükləmələr və yükləmələr üçün ümumi inkişaf_ağrısı."""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["▰" for i in range(math.floor(percentage / 10))]),
            "".join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            await event.edit(
                "{}\nFayl adı: `{}`\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """İnsan tərəfindən oxunaqlı bir formatda çıxışlar"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def time_formatter(milliseconds: int) -> str:
    """İnsan tərəfindən oxunaqlı bir formatda çıxışlar"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " Gün(s), ") if days else "")
        + ((str(hours) + " saaat(s), ") if hours else "")
        + ((str(minutes) + " dəqiqə(s), ") if minutes else "")
        + ((str(seconds) + " saniyə(s), ") if seconds else "")
        + ((str(milliseconds) + " millisaniyə(s), ") if milliseconds else "")
    )
    return tmp[:-2]


@borg.on(admin_cmd(pattern="yt(a|v) (.*)"))
@borg.on(sudo_cmd(pattern="yt(a|v) (.*)", allow_sudo=True))
async def download_video(v_url):
    """ .Ytdl əmri üçün YouTube-dan və bir çox başqa saytdan media yükləyin."""
    url = v_url.pattern_match.group(2)
    type = v_url.pattern_match.group(1).lower()
    friday = await edit_or_reply(v_url, "Endirməyə çalışıram ......")
    await friday.edit("`Yükləməyə hazırlaşır ...`")

    if type == "a":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "480",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        video = False
        song = True

    elif type == "v":
        opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
        song = False
        video = True

    try:
        await friday.edit("`Məlumat alınır, xahiş edirəm gözləyin ..`")
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url)
    except DownloadError as DE:
        await friday.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await friday.edit("`Endirmə məzmunu çox qısa idi.`")
        return
    except GeoRestrictedError:
        await friday.edit(
            "`Veb sayt tərəfindən qoyulmuş coğrafi məhdudiyyətlər səbəbindən video coğrafi məkandan əldə edilə bilməz.`"
        )
        return
    except MaxDownloadsReached:
        await friday.edit("`Maksimum yükləmə limitinə çatıldı.`")
        return
    except PostProcessingError:
        await friday.edit("`Sonrakı işləmə zamanı bir xəta baş verdi.`")
        return
    except UnavailableVideoError:
        await friday.edit("`Media tələb olunan formatda mövcud deyil.`")
        return
    except XAttrMetadataError as XAME:
        await friday.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await friday.edit("`Məlumat çıxarılması zamanı xəta baş verdi.`")
        return
    except Exception as e:
        await friday.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await friday.edit(
            f"`Mahnı yükləməyə hazırlaşır:`\
        \n**{ytdl_data['başlıq']}**\
        \nby *{ytdl_data['yükləyici']}*"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(
                    duration=int(ytdl_data["müddəti"]),
                    title=str(ytdl_data["başlıq"]),
                    performer=str(ytdl_data["yükləyici"]),
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, v_url, c_time, "Yüklənir ..", f"{ytdl_data['Başlıq]}.mp3"
                )
            ),
        )
        os.remove(f"{ytdl_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await friday.edit(
            f"`Video yükləməyə hazırlaşır:`\
        \n**{ytdl_data['başlıq']}**\
        \nby *{ytdl_data['yükləyici']}*"
        )
        await v_url.client.send_file(
            v_url.chat_id,
            f"{ytdl_data['id']}.mp4",
            supports_streaming=True,
            caption=ytdl_data["başlıq"],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d, t, v_url, c_time, "Yüklənir ..", f"{ytdl_data['başlıq']}.mp4"
                )
            ),
        )
        os.remove(f"{ytdl_data['id']}.mp4")
        await v_url.delete()
