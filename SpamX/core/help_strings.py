import os, re


hndlr = os.getenv("HNDLR")
if not hndlr:
  hndlr = "."

help_text = f"""
**𝐻𝐸𝐿𝒫 𝑀𝐸𝒩𝒰 𝒪𝐹 𝒯𝐻𝒰𝒟𝐸𝑅 𝒳 🍷!**

𝐹𝓊𝓃𝒸𝓉𝒾𝑜𝓃𝓈/𝑀𝑜𝒹𝓊𝓁𝑒𝓈 𝒶𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 ⬇️

=> `𝒮𝒫𝒜𝑀` , `𝑅𝒜𝐼𝒟` , `𝒪𝒲𝒩𝐸𝑅` , `𝒟𝐼𝑅𝐸𝒞𝒯𝑀𝐸𝒮𝒮𝒜𝒢𝐸` , `𝒜𝒟𝑀𝐼𝒩` , `𝒞𝒪𝑅𝐸` , `𝒮𝒰𝒟𝒪𝒮` , `𝒢𝐿𝒪𝐵𝒜𝐿` , `𝒫𝑅𝒪𝐹𝐼𝐿𝐸` , `𝒥𝒪𝐼𝒩 𝐿𝐸𝒜𝒱𝐸` , `𝐼𝒩𝐹𝒪`

𝒯𝓎𝓅𝑒 `{hndlr}help` (𝑀𝑜𝒹𝓊𝓁𝑒 𝓃𝒶𝓂𝑒) | 𝐵𝑜𝓉'𝓁𝓁 𝑔𝒾𝓋𝑒 𝒾𝓃𝒻𝑜/𝓊𝓈𝒶𝑔𝑒 𝑜𝒻
𝓉𝒽𝒶𝓉 𝓂𝑜𝒹𝓊𝓁𝑒.

𝐸𝓍𝒶𝓂𝓅𝓁𝑒: `{hndlr}𝒽𝑒𝓁𝓅 𝒸𝑜𝓇𝑒`
"""

spam_text = f"""
**𝑀𝑜𝒹𝓊𝓁𝑒 𝓃𝒶𝓂𝑒: 𝒮𝓅𝒶𝓂**

𝒜𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 𝒸𝑜𝓂𝓂𝒶𝓃𝒹𝓈 𝒶𝓃𝒹 𝓉𝒽𝑒𝓇𝑒 𝒰𝓈𝒶𝑔𝑒 ⬇️

•) {hndlr}𝓈𝓅𝒶𝓂 [𝒸𝑜𝓊𝓃𝓉𝓈] [𝓂𝑒𝓈𝓈𝒶𝑔𝑒]
•) {hndlr}𝒹𝑒𝓁𝒶𝓎𝓈𝓅𝒶𝓂 [𝒹𝑒𝓁𝒶𝓎 𝒾𝓃 𝓈𝑒𝒸𝓈.] [𝒞𝑜𝓊𝓃𝓉𝓈] [𝓂𝑒𝓈𝓈𝒶𝑔𝑒]
•) {hndlr}𝓅𝑜𝓇𝓃𝓈𝓅𝒶𝓂 [𝒸𝑜𝓊𝓃𝓉𝓈]
•) {hndlr}𝒽𝒶𝓃𝑔𝑒 [𝒸𝑜𝓊𝓃𝓉𝓈]
•) {hndlr}𝓊𝓈𝓅𝒶𝓂 [𝓂𝑒𝓈𝓈𝒶𝑔𝑒]
•) {hndlr}𝒶𝒷𝓊𝓈𝑒 [𝒸𝑜𝓊𝓃𝓉𝓈 𝑜𝓇 𝓁𝑒𝒶𝓋𝑒]
"""

raid_text = f"""
**𝑀𝑜𝒹𝓊𝓁𝑒 𝓃𝒶𝓂𝑒: 𝑅𝒶𝒾𝒹**

𝒜𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 𝒸𝑜𝓂𝓂𝒶𝓃𝒹𝓈 𝒶𝓃𝒹 𝓉𝒽𝑒𝓇𝑒 𝒰𝓈𝒶𝑔𝑒 ⬇️

•) {hndlr}𝓇𝒶𝒾𝒹 [𝒸𝑜𝓊𝓃𝓉𝓈] [𝓊𝓈𝑒𝓇𝓃𝒶𝓂𝑒 𝑜𝓇 𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝓊𝓈𝑒𝓇]
•) {hndlr}𝓊𝓇𝒶𝒾𝒹 [𝒰𝓈𝑒𝓇𝓃𝒶𝓂𝑒 𝑜𝓇 𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝓊𝓈𝑒𝓇]
•) {hndlr}𝓇𝑒𝓅𝓁𝓎𝓇𝒶𝒾𝒹 [𝓊𝓈𝑒𝓇𝓃𝒶𝓂𝑒 𝑜𝓇 𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝓊𝓈𝑒𝓇]
•) {hndlr}𝒹𝓇𝑒𝓅𝓁𝓎𝓇𝒶𝒾𝒹 [𝓊𝓈𝑒𝓇𝓃𝒶𝓂𝑒 𝑜𝓇 𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝓊𝓈𝑒𝓇]
"""

dm_text = f"""
**𝑀𝑜𝒹𝓊𝓁𝑒 𝓃𝒶𝓂𝑒: 𝒟𝒾𝓇𝑒𝒸𝓉 𝑀𝑒𝓈𝓈𝒶𝑔𝑒**

𝒜𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 𝒸𝑜𝓂𝓂𝒶𝓃𝒹𝓈 𝒶𝓃𝒹 𝓉𝒽𝑒𝓇𝑒 𝒰𝓈𝒶𝑔𝑒 ⬇️

•) {hndlr}𝒹𝓂 [𝓊𝓈𝑒𝓇𝓃𝒶𝓂𝑒 𝑜𝓇 𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝓊𝓈𝑒𝓇] [𝓂𝑒𝓈𝓈𝒶𝑔𝑒]
•) {hndlr}𝒹𝓂𝓈𝓅𝒶𝓂 [𝓊𝓈𝑒𝓇] [𝒸𝑜𝓊𝓃𝓉𝓈] [𝓂𝑒𝓈𝓈𝒶𝑔𝑒]
•) {hndlr}𝒹𝓂𝓇𝒶𝒾𝒹 [𝒸𝑜𝓊𝓃𝓉𝓈] [𝓊𝓈𝑒𝓇𝓃𝒶𝓂𝑒 𝑜𝓇 𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝓊𝓈𝑒𝓇]
"""

admin_text = f"""
**𝑀𝑜𝒹𝓊𝓁𝑒 𝓃𝒶𝓂𝑒: 𝒜𝒹𝓂𝒾𝓃**

𝒜𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 𝒸𝑜𝓂𝓂𝒶𝓃𝒹𝓈 𝒶𝓃𝒹 𝓉𝒽𝑒𝓇𝑒 𝒰𝓈𝒶𝑔𝑒 ⬇️

•) {hndlr}𝒷𝒶𝓃 [𝓊𝓈𝑒𝓇]
•) {hndlr}𝓊𝓃𝒷𝒶𝓃 [𝓊𝓈𝑒𝓇]
•) {hndlr}𝓅𝓇𝑜𝓂𝑜𝓉𝑒 [𝓊𝓈𝑒𝓇]
•) {hndlr}𝒹𝑒𝓂𝑜𝓉𝑒 [𝓊𝓈𝑒𝓇]
•) {hndlr}𝓅𝒾𝓃 [𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝓂𝑒𝓈𝓈𝒶𝑔𝑒]
•) {hndlr}𝓊𝓃𝓅𝒾𝓃 [𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝓂𝑒𝓈𝓈𝒶𝑔𝑒]
•) {hndlr}𝓅𝓊𝓇𝑔𝑒 [𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝓂𝑒𝓈𝓈𝒶𝑔𝑒]
"""

core_text = f"""
**𝓜𝓸𝓭𝓾𝓵𝓮 𝓷𝓪𝓶𝓮: 𝓒𝓸𝓻𝓮**

𝓐𝓿𝓪𝓲𝓵𝓪𝓫𝓵𝓮 𝓬𝓸𝓶𝓶𝓪𝓷𝓭𝓼 𝓪𝓷𝓭 𝓽𝓱𝓮𝓻𝓮 𝓤𝓼𝓪𝓰𝓮 ⬇️

•) {hndlr}𝓇𝑒𝓅𝑜𝓇𝓉 [𝓊𝓈𝑒𝓇] [𝑅𝟩 𝒷𝒶𝓃 𝒸𝑜𝒹𝑒] [𝓉𝑒𝓁𝑒𝑔𝓇𝒶𝓅𝒽 𝓁𝒾𝓃𝓀 𝒶𝓈 𝓅𝓇𝑜𝑜𝒻]
•) {hndlr}𝓈𝓉𝒶𝓉𝓈
•) {hndlr}𝓈𝑒𝓉𝓋𝒶𝓇 [𝓋𝒶𝓇 𝓃𝒶𝓂𝑒] [𝓀𝑒𝓎 𝓋𝒶𝓁𝓊𝑒] (𝐼𝓉 𝓂𝒶𝓎 𝒷𝑒 𝓊𝓈𝑒𝒻𝓊𝓁)
•) {hndlr}𝑔𝑒𝓉𝓋𝒶𝓇 (𝓉𝑜 𝑔𝑒𝓉 𝒶𝓁𝓁 𝒱𝒶𝓇𝓈 𝓃𝒶𝓂𝑒)
•) {hndlr}𝓁𝒾𝓂𝒾𝓉 (𝓉𝑜 𝒸𝒽𝑒𝒸𝓀 @𝒮𝓅𝒶𝓂𝒷𝑜𝓉 𝓁𝒾𝓂𝒾𝓉)
•) {hndlr}𝓉𝑒𝓁𝑒𝑔𝓇𝒶𝓅𝒽 [𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝑀𝑒𝒹𝒾𝒶]
"""

sudos_text = f"""
**𝒽𝓃𝒹𝓁𝑀𝑜𝒹𝓊𝓁𝑒 𝓃𝒶𝓂𝑒: 𝒮𝓊𝒹𝑜𝓈**

𝒜𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 𝒸𝑜𝓂𝓂𝒶𝓃𝒹𝓈 𝒶𝓃𝒹 𝓉𝒽𝑒𝓇𝑒 𝒰𝓈𝒶𝑔𝑒 ⬇️

•) {hndlr}𝒶𝒹𝒹𝓈𝓊𝒹𝑜 [𝓊𝓈𝑒𝓇] (𝐹𝒾𝓁𝓁 𝒟𝒜𝒯𝒜𝐵𝒜𝒮𝐸_𝒰𝑅𝐿 𝒻𝑜𝓇 𝓈𝓂𝑜𝑜𝓉𝒽 𝓊𝓈𝑒)
•) {hndlr}𝓇𝓂𝓈𝓊𝒹𝑜 [𝓊𝓈𝑒𝓇] (𝐹𝒾𝓁𝓁 𝒟𝒜𝒯𝒜𝐵𝒜𝒮𝐸_𝒰𝑅𝐿 𝒻𝑜𝓇 𝓈𝓂𝑜𝑜𝓉𝒽 𝓊𝓈𝑒)
•) {hndlr}𝓈𝓊𝒹𝑜𝓁𝒾𝓈𝓉
"""

global_text = f"""
**𝑀𝑜𝒹𝓊𝓁𝑒 𝓃𝒶𝓂𝑒: 𝒢𝓁𝑜𝒷𝒶𝓁**

𝒜𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 𝒸𝑜𝓂𝓂𝒶𝓃𝒹𝓈 𝒶𝓃𝒹 𝓉𝒽𝑒𝓇𝑒 𝒰𝓈𝒶𝑔𝑒 ⬇️

•) {hndlr}𝑔𝒷𝒶𝓃 [𝓊𝓈𝑒𝓇] (𝒟𝒜𝒯𝒜𝐵𝒜𝒮𝐸_𝒰𝑅𝐿 𝓇𝑒𝓆𝓊𝒾𝓇𝑒𝒹 𝒾𝓃 𝓉𝒽𝒾𝓈 𝒞𝑀𝒟)
•) {hndlr}𝓊𝓃𝑔𝒷𝒶𝓃 [𝓊𝓈𝑒𝓇] (𝒟𝒜𝒯𝒜𝐵𝒜𝒮𝐸_𝒰𝑅𝐿 𝓇𝑒𝓆𝓊𝒾𝓇𝑒𝒹 𝒾𝓃 𝓉𝒽𝒾𝓈 𝒞𝑀𝒟)
•) {hndlr}𝑔𝒷𝒶𝓃𝓁𝒾𝓈𝓉
•) {hndlr}𝑔𝓅𝓇𝑜𝓂𝑜𝓉𝑒 [𝓊𝓈𝑒𝓇]
•) {hndlr}𝑔𝒹𝑒𝓂𝑜𝓉𝑒 [𝓊𝓈𝑒𝓇]
"""

profile_text = f"""
**𝑀𝑜𝒹𝓊𝓁𝑒 𝓃𝒶𝓂𝑒: 𝒫𝓇𝑜𝒻𝒾𝓁𝑒**

𝒜𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 𝒸𝑜𝓂𝓂𝒶𝓃𝒹𝓈 𝒶𝓃𝒹 𝓉𝒽𝑒𝓇𝑒 𝒰𝓈𝒶𝑔𝑒 ⬇️

•) {hndlr}𝓈𝑒𝓉𝓅𝒾𝒸 [𝓇𝑒𝓅𝓁𝓎 𝓉𝑜 𝑀𝑒𝒹𝒾𝒶]
•) {hndlr}𝓈𝑒𝓉𝓃𝒶𝓂𝑒 [𝐹𝒾𝓇𝓈𝓉 𝓃𝒶𝓂𝑒] [𝓁𝒶𝓈𝓉 𝓃𝒶𝓂𝑒 (𝑜𝓅𝓉𝒾𝑜𝓃𝓈𝒾) ]
•) {hndlr}𝓈𝑒𝓉𝒷𝒾𝑜 [𝒩𝑒𝓌 𝒷𝒾𝑜]
•) {hndlr}𝒸𝓁𝑜𝓃𝑒 [𝓊𝓈𝑒𝓇] (𝓉𝑜 𝒸𝓁𝑜𝓃𝑒 𝓈𝑜𝓂𝑒𝑜𝓃𝑒'𝓈 𝓅𝓇𝑜𝒻𝒾𝓁𝑒]
•) {hndlr}𝓇𝑒𝓋𝑒𝓇𝓉 (𝒯𝑜 𝓇𝑒𝓂𝑜𝓋𝑒 𝒸𝓁𝑜𝓃𝑒)
"""

owner_text = f"""
**𝑀𝑜𝒹𝓊𝓁𝑒 𝓃𝒶𝓂𝑒: 𝒪𝓌𝓃𝑒𝓇 𝓈𝓉𝓊𝒻𝒻**

𝒜𝓋𝒶𝒾𝓁𝒶𝒷𝓁𝑒 𝒸𝑜𝓂𝓂𝒶𝓃𝒹𝓈 𝒶𝓃𝒹 𝓉𝒽𝑒𝓇𝑒 𝒰𝓈𝒶𝑔𝑒 ⬇️

•) {hndlr}𝑒𝓋𝒶𝓁 [𝒸𝑜𝒹𝑒]
•) {hndlr}𝒷𝓇𝑜𝒶𝒹𝒸𝒶𝓈𝓉 [𝓂𝑒𝓈𝓈𝒶𝑔𝑒]
•) {hndlr}𝓂𝓈𝑔𝒶𝓁𝓁 [𝓂𝑒𝓈𝓈𝒶𝑔𝑒] (𝒾𝓃 𝑔𝓇𝑜𝓊𝓅𝓈 𝑜𝓃𝓁𝓎)
•) {hndlr}𝓈𝒸𝓇𝒶𝓅𝑒 [𝐹𝓇𝑜𝓂 𝑔𝓇𝑜𝓊𝓅]
•) {hndlr}𝒷𝒶𝓃𝒶𝓁𝓁
"""

joinleave_text = f"""
**𝓜𝓸𝓭𝓾𝓵𝓮 𝓷𝓪𝓶𝓮: 𝓙𝓸𝓲𝓷 𝓵𝓮𝓪𝓿𝓮**

𝓐𝓿𝓪𝓲𝓵𝓪𝓫𝓵𝓮 𝓬𝓸𝓶𝓶𝓪𝓷𝓭𝓼 𝓪𝓷𝓭 𝓽𝓱𝓮𝓻𝓮 𝓤𝓼𝓪𝓰𝓮 ⬇️

•) {hndlr}𝒿𝑜𝒾𝓃 [𝑔𝓇𝑜𝓊𝓅 𝓊𝓈𝑒𝓇𝓃𝒶𝓂𝑒]
•) {hndlr}𝓁𝑒𝒶𝓋𝑒 [𝑔𝓇𝑜𝓊𝓅 𝓊𝓈𝑒𝓇𝓃𝒶𝓂𝑒 𝑜𝓇 𝐼𝒟]
"""

info_text = f"""
**𝓜𝓸𝓭𝓾𝓵𝓮 𝓷𝓪𝓶𝓮: 𝓘𝓷𝓯𝓸**

𝓐𝓿𝓪𝓲𝓵𝓪𝓫𝓵𝓮 𝓬𝓸𝓶𝓶𝓪𝓷𝓭𝓼 𝓪𝓷𝓭 𝓽𝓱𝓮𝓻𝓮 𝓤𝓼𝓪𝓰𝓮 ⬇️

•) {hndlr}𝒯𝒽𝓊𝓃𝒹𝑒𝓇𝒳
•) {hndlr}𝒾𝓃𝒻𝑜 [𝒰𝓈𝑒𝓇]
•) {hndlr}𝒾𝒹 [𝓊𝓈𝑒𝓇]
"""

def check_string(text):
   if re.search("spam".lower(), text.lower()):
      return "spam"
   if re.search("raid".lower(), text.lower()):
      return "raid"
   if re.search("owner".lower(), text.lower()):
      return "owner"
   if re.search("directmessage|direct_message".lower(), text.lower()):
      return "dm"
   if re.search("admin".lower(), text.lower()):
      return "admin"
   if re.search("core".lower(), text.lower()):
      return "core"
   if re.search("sudos|sudo".lower(), text.lower()):
      return "sudos"
   if re.search("global".lower(), text.lower()):
      return "global"
   if re.search("profile".lower(), text.lower()):
      return "profile"
   if re.search("join|leave|joinleave".lower(), text.lower()):
      return "joinleave"
   if re.search("info".lower(), text.lower()):
      return "info"

async def help_return(text):
   if check_string(text) == "spam":
      return spam_text
   elif check_string(text) == "raid":
      return raid_text
   elif check_string(text) == "dm":
      return dm_text
   elif check_string(text) == "admin":
      return admin_text
   elif check_string(text) == "core":
      return core_text
   elif check_string(text) == "sudos":
      return sudos_text
   elif check_string(text) == "global":
      return global_text
   elif check_string(text) == "profile":
      return profile_text
   elif check_string(text) == "owner":
      return owner_text
   elif check_string(text) == "joinleave":
      return joinleave_text
   elif check_string(text) == "info":
      return info_text
   else:
      return help_text
