import nltk, numpy, tflearn, tensorflow, random, json

class ChatBot:
    def __init__(self, intents_path):
        self.stemmer = nltk.stem.lancaster
        self.words = []
        self.labels = []
        self.docs_x = []
        self.docs_y = []
        self.training = []
        self.output = []

        self.prepare_intents(intents_path)
        self.word_stemming()
        self.prepare_bag_of_words(0)

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
    
    def prepare_bag_of_words(self):
        out_empty = [0 for _ in range(len(self.labels))]

        for x, doc in enumerate(self.docs_x):
            bag = []
            wrds = [self.stemmer.stem(w.lower()) for w in doc]
        
            for w in self.words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)
            
            output_row = out_empty[:]
            output_row[self.labels.index(docs_y[x])] = 1

            self.training.append(bag)
            self.output.append(output_row)
        
        self.training = numpy.array(self.training)
        self.output = numpy.array(self.output)

        

    


