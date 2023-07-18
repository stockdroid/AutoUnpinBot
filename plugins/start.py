from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Buonasera! Sono solo un bot che unpinna i messaggi dei canali automaticamente. Aggiungimi al gruppo con il permesso di fissare per farmi togliere il pin automaticamente!")
