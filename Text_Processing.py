# pip install spacy
# python -m spacy download en_core_web_sm
import spacy
from collections import Counter

class Text_Processing(object):
    
    # Class constructor
    def __init__(self, text):
        self.text = text
        self.nlp = spacy.load("en_core_web_sm")
    
    # Returns a list of 5 of the most frequent words that are not stop words and not punctuation
    def getTopics(self):
        doc = self.nlp(self.text)
        potentialTopics = [token.text for token in doc if not token.is_stop and not token.is_punct]
        freq = Counter(potentialTopics)
        listOfTopics = freq.most_common(5)
        return listOfTopics
    
    # Returns a list of sentences
    def getSentences(self):
        doc = self.nlp(self.text)
        sentences = list(doc.sents)
        return sentences



