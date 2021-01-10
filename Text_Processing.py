# pip install spacy
# python -m spacy download en_core_web_sm
import spacy
from collections import Counter

class Text_Processing(object):
    
    # Class constructor
    def __init__(self, text):
        self.text = text
        self.nlp = spacy.load("en_core_web_sm")

    # Removes the different types of whitespaces in the text file
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
        listOfTopics = self.checkTopFive(freq)
        return listOfTopics
    
    # Returns a list of sentences
    def getSentences(self):
        doc = self.nlp(self.text)
        sentences = list(doc.sents)
        return sentences

    #def checkTheTopFive(self, dictionary_var):
        

    def checkTopFive(self, dict):
        checker = True
        key_array = []
        index_storing = []
        boolean_storing = []
        while(checker):
            checker = False
            key_array = dict.most_common(5)
            for i in range(len(key_array)-1):
                key = key_array[i][0].lower()
                key2 = key_array[i+1][0].lower()
                checker = self.areKeysSame(key, i, key2, i+1, index_storing, boolean_storing)

            if checker == True:
                keyFinal = key_array[i][1] + key_array[i+1][1]
                key_array.pop(key_array.index((key_array[i][0], key_array[i][1])))
                key_array.pop(key_array.index((key_array[i+1][0], key_array[i+1][1])))
                key_array.append((key_array[i][0], keyFinal))
                
        return key_array
        
            
    def areKeysSame(self, key1, key1_index, key2, key2_index, index_store, bool_store):
        if key1 == key2:
            #store both the indexes
            index_store.append = key1_index
            index_store.append = key2_index
            return True
        elif key1 != key2:
            return False
            
            
            
        
            
            

    

