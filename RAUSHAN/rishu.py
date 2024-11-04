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
                ],
                [
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/RADHE_MUSIC_ROBOT"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/vip_music_vc_bot"),
              ],
              [
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/RishuXmusicXbot"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://t.me/KhushiXchatbot"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://t.me/RishuStringBot"),
InlineKeyboardButton("𝗖𝗔𝗠𝗘𝗥𝗔 𝗛𝗔𝗖𝗞", url=f"https://t.me/RISHU_CAMERA_ROBOT"),
],
[
              InlineKeyboardButton("𝗣𝗛𝗜𝗦𝗛𝗜𝗡𝗚 𝗕𝗢𝗧", url=f"https://t.me/Rishabh_hackbot"),
              InlineKeyboardButton("𝗙𝗜𝗟𝗘 𝗦𝗛𝗔𝗥𝗜𝗡𝗚", url=f"https://t.me/Share_file_robot"),
              ],
              [
              InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗜𝗡𝗙𝗢", url=f"https://t.me/CHAT_INFO_ROBOT"),
InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘 𝗕𝗢𝗧", url=f"https://t.me/Rishu_movie_bot"),
],
[
InlineKeyboardButton("𝗙𝗢𝗡𝗧 𝗖𝗛𝗔𝗡𝗚𝗘𝗥", url=f"https://t.me/RishuXfrontXbot"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗚𝗣𝗧", url=f"https://t.me/Gpt_pro_robot"),
]               
            ]
        )
    )