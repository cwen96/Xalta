# pip install spacy
# python -m spacy download en_core_web_sm
import spacy
from collections import Counter

class Text_Processing(object):
    
    # Class constructor
    def __init__(self, text):
        self.text = text
        self.nlp = spacy.load("en_core_web_sm")

    def whitespaceRemover(self, string):
        text2 = string.replace("\n","")
        text3 = text2.replace("\r","")
        return text3
    
    # Returns a list of 5 of the most frequent words that are not stop words and not punctuation
    def getTopics(self):
        text2 = self.whitespaceRemover(self.text)
        doc = self.nlp(text2)
        potentialTopics = [token.text for token in doc if not token.is_stop and not token.is_punct]
        freq = Counter(potentialTopics)
        del freq[" "]
        listOfTopics = freq.most_common(5)
        return listOfTopics
    
    # Returns a list of sentences
    def getSentences(self):
        doc = self.nlp(self.text)
        sentences = list(doc.sents)
        return sentences

    