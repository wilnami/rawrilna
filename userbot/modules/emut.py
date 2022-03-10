from platform import uname
import time
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^.emut(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    time.sleep(1)
    await typew.edit("`sedang mengemut...`")
    # terus jeda 1 detik
    time.sleep(2)
    await typew.edit("`muah muah muah muah`")
    time.sleep(1)
    await typew.edit("`muah muah muah muah\nmuah muah muah muah`")
    time.sleep(1)
    await typew.edit("`muah muah muah muah\nmuah muah muah muah\nmuah muah muah muah`")
    time.sleep(1)
    await typew.edit("`muah muah muah muah\nmuah muah muah muah\nmuah muah muah muah\nmuah muah muah muah`")
    time.sleep(5)
    await typew.edit("`berhasil mengemut`")

CMD_HELP.update({
    "emut":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.emut`\
\n↳ : Untuk mengemut"
})
