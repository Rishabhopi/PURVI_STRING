from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("repo"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://envs.sh/Amn.jpg",
        caption=f"""**  ʜᴇʏ  {msg.from_user.mention}  ✤,

✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ ʀɪsʜᴜ sᴛʀɪɴɢ™ ʙᴏᴛ ✪
 
 ❍ • ʙsᴅᴋ ᴋᴇᴛᴀɴɪ ʙᴀʀʀ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ •
 
 ❍ • ᴘᴇʜʟᴇ ʀᴇᴘᴏ ʜᴇ ᴅᴀ ᴅᴇʏᴀ ʜᴜ•
 
 ❍ • ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ❍ • ᴀᴜʀ ʀᴇᴘᴏs ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ •
 
 ❍ • ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ Rɪsʜᴜ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
 ❍ • ʀᴀᴅʜᴇ ʀᴀᴅʜᴇ • ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="❍ 𝐒ᴛʀɪɴɢ ❍", url="https://t.me/rishustringbot")
                ],
                [
                    InlineKeyboardButton("❍ 𝐒ᴜᴘᴘᴏʀᴛ ❍", url="https://t.me/Ur_support07"),
                    InlineKeyboardButton("❍ 𝐔ᴘᴅᴀᴛᴇ ❍", url="https://t.me/ur_rishu_143")
                ],
                [
                    InlineKeyboardButton("❍ 𝐀ʟʟ 𝐁ᴏᴛ𝐬 ❍", url="https://t.me/Vip_robotz/4"),
                    InlineKeyboardButton("❍ 𝐌ᴜ𝐬ɪᴄ 𝐁ᴏᴛ ❍", url="https://t.me/Vip_music_vc_bot")
                ]                
            ]
        )
    )