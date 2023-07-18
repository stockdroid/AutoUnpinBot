from pyrogram import Client
import json

config = json.load(open("./configs/config.json"))

client = Client(
    "Bot",
    api_id=config["API_ID"],
    api_hash=config["API_HASH"],
    bot_token=config["BOT_TOKEN"],
    plugins=dict(root="plugins")
).run()

