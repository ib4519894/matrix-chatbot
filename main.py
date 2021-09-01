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
    print(f"message {message}")
    match = botlib.MessageMatch(room, message, bot, prefix)

    if match.is_not_from_this_bot() and match.prefix():
        print("matched")
        response = str(cbot.respond(message.body[2:]))
        print(f"response - {response}")
        await bot.api.send_text_message(room.room_id, response)

chat_log = []
@bot.listener.on_message_event
async def train_from_chat(room, message):
    global chat_log
    match = botlib.MessageMatch(room, message, bot)
    data = str(message.body)
    if data.startswith("c!"):
        data = data[2:]
    chat_log.append(data)
    if len(chat_log) > 15:
        print(f"training on data {chat_log}")
        cbot.list_trainer.train(chat_log)
        chat_log = []


bot.run()