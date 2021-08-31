import chatterbot

class CustomChatterBot:
    def __init__(self, name="Matrix-Chatbot", learning=True):
        self.chatterbot = chatterbot.ChatBot(name="placeholder_name", read_only=False, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
        self.response_training_data = {
            "greetings":["hello", "hi"],
            "salutations":["bye, goodbye"]
        }
        self.corpus_training_data = [
            "chatterbot.corpus.english"
        ]
    
    def train(self):
        list_trainer = chatterbot.trainers.ListTrainer(self.chatterbot)
        for label, response_list in response_training_data:
            print(f"Training {label}")
            list_trainer.train(response_list)
        
        corpus_trainer = chatterbot.trainers.ChatterBotCorpusTrainer(self.chatterbot)
        for corpus in self.corpus_training_data:
            print(f"Training {corpus}")
            corpus_trainer.train(corpus)
        
        print("Training Complete")
    
    def respond(self, prompt : str):
        return self.chatterbot.get_response(prompt)