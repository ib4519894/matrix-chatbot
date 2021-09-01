import chatterbot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

class CustomChatterBot:
    def __init__(self, name="Matrix-Chatbot", learning=True):
        self.chatterbot = chatterbot.ChatBot(name="placeholder_name", read_only=False, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
        self.response_training_data = {
            "greetings":["hello", "hi"],
            "salutations":["bye, goodbye"],
            "numbers":[str(x) for x in range(0, 10)]
        }
        self.corpus_training_data = [
            "chatterbot.corpus.english"
        ]
    
    def train(self):
        self.list_trainer = ListTrainer(self.chatterbot)
        for label, response_list in self.response_training_data.items():
            print(f"Training {label}")
            self.list_trainer.train(response_list)
        
        corpus_trainer = ChatterBotCorpusTrainer(self.chatterbot)
        for corpus in self.corpus_training_data:
            print(f"Training {corpus}")
            corpus_trainer.train(corpus)
        
        print("Training Complete")
    
    def respond(self, prompt : str):
        return self.chatterbot.get_response(prompt)