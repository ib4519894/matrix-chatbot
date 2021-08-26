import (
    nltk,
    numpy,
    tflearn,
    tensorflow,
    random,
    json
)

class ChatBot:
    def __init__(self, intents_path):
        self.prepare_intents(intents_path)

    def prepare_intents(self, intents_path):

        stemmer = nltk.stem.lancaster

        with open(intents_path, "r") as f:
            data = json.load(f)
        
        words = []
        labels = []
        docs_x = []
        docs_y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])
            
            if intent["tag"] not in labels:
                labels.append(intent["tag"])


