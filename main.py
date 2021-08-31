import bot

cbot = bot.CustomChatterBot()
cbot.train()

while True:
    print(cbot.respond(input("say something > ")))