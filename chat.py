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
        self.stemmer = nltk.stem.lancaster
        self.words = []
        self.labels = []
        self.docs_x = []
        self.docs_y = []

        self.prepare_intents(intents_path)
        self.word_stemming()

    def prepare_intents(self, intents_path):
        with open(intents_path, "r") as f:
            data = json.load(f)
        
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                self.words.extend(wrds)
                self.docs_x.append(wrds)
                self.prepare_intentsdocs_y.append(intent["tag"])
            
            if intent["tag"] not in self.labels:
                self.labels.append(intent["tag"])
    
    def word_stemming(self):
        self.words = [self.stemmer.stem(w.lower()) for w in self.words if w != "?"]
        self.words = sorted(list(set(self.words)))

        self.labels = sorted(self.labels)
    
    

