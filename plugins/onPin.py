from pyrogram import Client

@Client.on_raw_update()
async def raw_update(client, update, users, chats):
    try:
        if update.message.fwd_from is not None:
            if update.message.fwd_from.channel_post is not None:
                await client.unpin_chat_message(chat_id=f"-100{update.message.peer_id.channel_id}", message_id=update.message.id)
    except:
        pass
