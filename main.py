# Based on https://www.upgrad.com/blog/how-to-make-chatbot-in-python/
import bot

cbot = bot.CustomChatterBot()
cbot.train()

while True:
    print(cbot.respond(input("say something > ")))