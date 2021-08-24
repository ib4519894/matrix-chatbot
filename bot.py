import simplematrixbotlib as botlib

with open(".env", "r") as f:
    env = f.readlines()
    creds = botlib.Creds(env[0][:-1], env[1][:-1], env[2])
bot = botlib.Bot(creds)
PREFIX = '!'

@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):

        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )

bot.run()