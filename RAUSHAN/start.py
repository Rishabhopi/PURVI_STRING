from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/6ksft0.jpg",
        caption=f"""**❍ » ʜᴇʏ  {msg.from_user.mention}  ✤,

❍ » ɪ ᴀᴍ{me2},

❍ » A sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.

❍ » ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

❍ » ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ᯓ𓆰𝅃꯭᳚ ⃪♔‌༎𝗥𝗜𝗦𝗛𝗨 ⃪𝄀꯭𝄄꯭ا✾༐𓂃⃪꯭,♡](tg://user?id={OWNER_ID}) ** !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="▪ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ▪️", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🔸 sᴜᴘᴘᴏʀᴛ🔸", url="https://t.me/PURVI_SUPPORT"),
                    InlineKeyboardButton("▫️ ᴜᴘᴅᴀᴛᴇs▫️", url="https://t.me/+Oh7OmMhAPKY5YTc9")
                ],
                [
                    InlineKeyboardButton("🔸 sᴏᴜʀᴄᴇ 🔸", url="https://github.com/TEAMPURVI/PURVI_STRING"),
                    InlineKeyboardButton("▫️ᴍᴜsɪᴄ ʙᴏᴛ▫️", url="https://t.me/PURVI_MUSIC_BOT")
                ]                
            ]
        )
    )