# Based on https://www.upgrad.com/blog/how-to-make-chatbot-in-python/
import chatterbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = chatterbot.ChatBot(name="placeholder_name", read_only=False, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

greetings = [
    "hello",
    "hi"
]

salutations = [
    "goodbye",
    "bye"
]

responses = (greetings, salutations)

list_trainer = ListTrainer(my_bot)
for item in responses:
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print(my_bot.get_response("bye"))
while True:
    print(my_bot.get_response(input("say something > ")))