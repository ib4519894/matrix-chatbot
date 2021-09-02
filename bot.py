import chatterbot
from chatterbot.trainers import ListTrainer
import os, json

class CustomChatterBot:
    def __init__(self, name="Matrix-Chatbot", learning=True):
        self.chatterbot = chatterbot.ChatBot(name="placeholder_name", read_only=False, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
        self.response_training_data = {}
        for file in os.listdir("./training_data"):
            filename = os.fsdecode(file)
            if filename.endswith(".json"):
                with open(os.path.join("./training_data", filename)) as f:
                    new_data = json.loads(f.read())
                    self.response_training_data = {**self.response_training_data, **new_data}
    
    def train(self):
        self.list_trainer = ListTrainer(self.chatterbot)
        for label, response_list in self.response_training_data.items():
            print(f"Training on data: {label}.yml")
            self.list_trainer.train(response_list)
        print("Training Complete")
    
    def respond(self, prompt : str):
        return self.chatterbot.get_response(prompt)