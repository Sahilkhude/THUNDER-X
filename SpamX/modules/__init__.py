from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "𝓣𝓗𝓤𝓝𝓓𝓔𝓡 𝓧 🍷"
pic = ALIVE_PIC if ALIVE_PIC else "https://graph.org/file/a4ce02f203c8c509a49ee.mp4"
amsg = ALIVE_MSG if ALIVE_MSG else "𝓣𝓗𝓤𝓝𝓓𝓔𝓡 𝓧 🍷"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
• {amsg} •

━───────╯•╰───────━
 • 𝓜𝓐𝓢𝓣𝓔𝓡 •  {owner_mention}
 • 𝓟𝓨𝓣𝓗𝓞𝓝 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 •  `{platform.python_version()}`
 • 𝓣𝓗𝓤𝓝𝓓𝓔𝓡 𝓧 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 •  `{__version__}`
 • 𝓟𝓨𝓡𝓞𝓖𝓡𝓐𝓜 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 •  `{pyro_vr}`
 • 𝓟𝓨 𝓣𝓗𝓤𝓝𝓓𝓔𝓡 𝓧 𝓥𝓔𝓡𝓢𝓘𝓞𝓝 •  `{pip_vr}`
 • 𝓒𝓗𝓐𝓝𝓝𝓔𝓛 •  @UNI_INDIA_0008
━───────╮•╭───────━
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
