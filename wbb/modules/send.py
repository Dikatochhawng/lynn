from pyrogram import filters
from wbb import app

@app.on_message(filters.command("snd") & ~filters.edited)
async def send(_, message):
  rsr = message.text.split(None, 1)[1]
  await app.send_message(rsr, disable_web_page_preview=True)
  await message.delete()
