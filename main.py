# Based on https://www.upgrad.com/blog/how-to-make-chatbot-in-python/
from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name="placeholder_name", read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])