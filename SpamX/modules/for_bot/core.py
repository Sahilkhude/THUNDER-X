"""
     Thunder X - Telegram Bots
           2024 - 2025
"""
import os, sys, asyncio, datetime, time, subprocess 
from .. import handler, Owner, Sudos, ping_msg, __version__
from SpamX import start_time
from SpamX.config import group_welcome

from pyrogram import Client, filters
from pyrogram.types import Message, ChatMemberUpdated
from pyrogram.enums import ChatType

from RiZoeLX.data import Variables, Variables_text
from RiZoeLX import Devs
from RiZoeLX.functions import get_time, delete_reply, Red7_Watch as oops_watch


@Client.on_message(filters.user(Sudos) & filters.command(["ping"], prefixes=handler))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      pong_msg = await e.reply("**𝒫𝑜𝓃𝑔 ! !**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await pong_msg.edit_text(f"⌾ {ping_msg} ⌾ \n\n ༝ 𝒫𝐼𝒩𝒢: `{ms}` ᴍs \n ༝ 𝒰𝒫𝒯𝐼𝑀𝐸: `{uptime}` \n ༝ 𝒱𝐸𝑅𝒮𝐼𝒪𝒩: `{__version__}`")
      
@Client.on_message(filters.me & filters.command(["ping"], prefixes=handler))
async def ping_me(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      try:
        pong_msg = await e.edit_text("**𝒫𝑜𝓃𝑔 ! !**")
      except:
        pong_msg = await e.reply("**𝒫𝑜𝓃𝑔 ! !**")
        await e.delete()    
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await pong_msg.edit_text(f"⌾ {ping_msg} ⌾ \n\n ༝ 𝒫𝐼𝒩𝒢: `{ms}` ᴍs \n ༝ 𝒰𝒫𝒯𝐼𝑀𝐸: `{uptime}` \n ༝ 𝒱𝐸𝑅𝒮𝐼𝒪𝒩: `{__version__}`")



@Client.on_message(filters.user(Owner) & filters.command(["getvars", "getvar"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["getvars", "getvar"], prefixes=handler))
async def all_vars(_, message: Message):
    await message.reply_text(f"All Variables given below 👇\n\n {Variables_text} \n\n © @KANU_0008")

@Client.on_message(filters.user(Sudos) & filters.command(["restart", "reboot"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["restart", "reboot"], prefixes=handler))
async def restarter(SpamX: Client, message: Message):
   await message.reply_text("**𝑅𝑒-𝓈𝓉𝒶𝓇𝓉𝒾𝓃𝑔...** \n 𝒫𝓁𝑒𝒶𝓈𝑒 𝓌𝒶𝒾𝓉 !")
   try:
     await SpamX.stop()
   except Exception as error:
     print(str(error))

   args = [sys.executable, "-m", "SpamX"]
   os.execl(sys.executable, *args)
   quit()
   

@Client.on_chat_member_updated(filters.group, group=69)
async def welcome_watcher(SpamX: Client, member: ChatMemberUpdated):
   if (
        member.new_chat_member
        and member.new_chat_member.status not in {CMS.BANNED, CMS.LEFT, CMS.RESTRICTED}
        and not member.old_chat_member
   ):
        pass
   else:
        return

   mai = await SpamX.get_me()
   user = member.new_chat_member.user if member.new_chat_member else member.from_user    
   if group_welcome:
      if user.id == mai.id:
         await SpamX.send_message(message.chat.id, "ThunderX Here. Powered by @KANU_0008!")
         return
      if user.id == Owner:
         await SpamX.send_message(message.chat.id, f"{user.mention} Welcome to {message.chat.title} my King 👑")
         return
      if user.id in Devs:
         await SpamX.send_message(message.chat.id, f"{user.mention} ThunderX's Devs joined👾")
         return
      if user.id in Sudos:
         await SpamX.send_message(message.chat.id, f"{user.mention} Whoa! The Prince just joined 🫠!")
         return
      await oops_watch(SpamX, member)
   else:
      if user.id == mai.id:
         return
      if user.id == Owner:
         return
      if user.id in Devs:
         return
      if user.id in Sudos:
         return
      await oops_watch(SpamX, member)

@Client.on_message(filters.user(Devs) & filters.command(["update"], prefixes=handler))
@Client.on_message(filters.user(Owner) & filters.command(["update"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["update"], prefixes=handler))
async def Update_SpamX(SpamX: Client, message: Message):
   try:
      out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
      if "Already up to date." in str(out):
         await message.reply_text("Its already up-to date!")
         return
      await message.reply_text(f"```{out}```")
   except Exception as e:
      await message.reply_text(str(e))
      return
   await message.reply_text("**𝒰𝓅𝒹𝒶𝓉𝑒𝒹 𝓌𝒾𝓉𝒽 𝓂𝒶𝒾𝓃 𝒷𝓇𝒶𝓃𝒸𝒽, 𝓇𝑒𝓈𝓉𝒶𝓇𝓉𝒾𝓃𝑔 𝓃𝑜𝓌.**")
   args = [sys.executable, "-m", "SpamX"]
   os.execl(sys.executable, *args)
   quit()

""" NOTE: This is an extra module! it may be useful """
@Client.on_message(filters.user(Devs) & filters.command(["setvar", "ossystem"], prefixes=handler))
@Client.on_message(filters.user(Owner) & filters.command(["setvar", "ossystem"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["setvar", "ossystem"], prefixes=handler))
async def os_system(SpamX: Client, message: Message):
    txt = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(txt) == 2:
       check_var = txt[0]
       if check_var in Variables:
          var = check_var
       else:
          await message.reply_text(f"Wrong variable! All Variables given below 👇\n\n {Variables_text} \n\n © @KANU_0008")
          return
       value = str(txt[1])
       try:
         os.system(f"dotenv set {var} {value}")
         await message.reply_text("𝓈𝓊𝒸𝒸𝑒𝓈𝓈 ✓ 𝓌𝒶𝒾𝓉 𝒻𝑜𝓇 𝓇𝑒-𝓈𝓉𝒶𝓇𝓉")
         args = [sys.executable, "-m", "SpamX"]
         os.execl(sys.executable, *args)
         quit()
       except Exception as error:
         await message.reply_text(f"Error: {error} \n\n Report in @UNI_INDIA_0000")
    else:
       await message.reply_text(f"**Wrong Usage** \n Syntax: {handler}setvar (var name) (value) \n\n Type `{handler}getvars` To get all Vars name!")
