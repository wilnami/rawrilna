from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^.hadeh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`mendapat tambahan 1 hadeh`")

CMD_HELP.update({
    "hadeh":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.hadeh`\
\n↳ : Untuk memberi hadeh"
})
