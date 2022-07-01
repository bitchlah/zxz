# inspiration from @greyyvbss
# modification of @punya_alby

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterPhotos


@ayiin_cmd(pattern="ppcp$")
async def _(event):
    try:
        fotbarnya = [
            fotbar
            async for fotbar in event.client.iter_messages(
                "@fotbarlyorax", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(fotbarnya),
            caption=f" Nih Kak PP Couple nya 😎 [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("PPCP nya Gada Karena Kamu Jelek _-.")


@ayiin_cmd(pattern="ppcp2$")
async def _(event):
    try:
        fotbarnya = [
            fotbar
            async for fotbar in event.client.iter_messages(
                "@fotbarpi", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(fotbarnya),
            caption=f" Nih Kak PP Couple nya 😎 [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("PPCP nya Gada Karena Kamu Jelek _-.")


@ayiin_cmd(pattern="ppcp3$")
async def _(event):
    try:
        fotbarnya = [
            fotbar
            async for fotbar in event.client.iter_messages(
                "@rp_fotbar", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(fotbarnya),
            caption=f" Nih Kak PP Couple nya 😎 [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("PPCP nya Gada Karena Kamu Jelek _-.")


CMD_HELP.update(
    {
        "albyppcouple": f"❖ **Plugin : **`ppcouple`\
        \n\n ┌❖ **Perintah :** `{cmd}ppcp`\
        \n └❖ **Berfungsi : **Untuk Mencari PP Couple secara random.\
        \n\n ┌❖ **Perintah :** `{cmd}ppcp2`\
        \n └❖ **Berfungsi : **Untuk Mencari PP Couple secara random versi kedua.\
        \n\n ┌❖ **Perintah :** `{cmd}ppcp3`\
        \n └❖ **Berfungsi : **Untuk Mencari PP Couple secara random versi ketiga.\
    "
    }
)
