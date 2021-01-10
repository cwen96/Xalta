# pip install spacy
# python -m spacy download en_core_web_sm
import spacy

class Text_Processing(object):
    
    def __init__(self, text):
        self.text = text
        self.nlp = spacy.load("en_core_web_sm")
    
    def getNouns(self):
        doc = self.nlp(self.text)
        nouns = [chunk.text for chunk in doc.noun_chunks]
        return nouns




