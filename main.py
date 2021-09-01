import bot
import simplematrixbotlib as botlib
import os

cbot = bot.CustomChatterBot()
cbot.train()

creds = botlib.Creds(os.getenv("MATRIX_BOT_HOMESERVER"), os.getenv("MATRIX_BOT_USERNAME"), os.getenv("MATRIX_BOT_PASSWORD"))
bot = botlib.Bot(creds)
prefix = "c!"

@bot.listener.on_message_event
async def respond_to_chat(room, message):
    match = botlib.MessageMatch(room, message, bot, prefix)

    if match.is_not_from_this_bot() and match.prefix():
        response = cbot.respond(message.body)
        await bot.api.send_text_message(room.room_id, response)

bot.run()