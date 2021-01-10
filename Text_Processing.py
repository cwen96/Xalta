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
        listOfTopics = self.checkTheTopFive(freq)
        return listOfTopics
    
    # Returns a list of sentences
    def getSentences(self):
        doc = self.nlp(self.text)
        sentences = list(doc.sents)
        return sentences

    def checkTheTopFive(self, dictionary_var):
        delList = []
        for i in range(len(dictionary_var)):
            for j in range(len(dictionary_var)-1):
                if j != i:
                    dupKeySum = 0
                    compare1 = list(dictionary_var.keys())[i]
                    compare2 = list(dictionary_var.keys())[j]
                    if compare1.lower() == compare2.lower() and compare1 not in delList and compare2 not in delList:
                        dupKeySum += dictionary_var[compare1]
                        dupKeySum += dictionary_var[compare2]
                        delList.append(compare1)
                        delList.append(compare2)
                        dictionary_var += {compare1.lower():dupKeySum}
        for value in delList:
            del dictionary_var[value]
        return dictionary_var.most_common(5)


    '''
    checker = True
    local_checker = True
    key_array = []
    while(checker):
        key_array = dictionary_var.most_common(5)
        print(key_array)
        for i in range(len(key_array)-1):
            key1 = key_array[i][0]
            key2 = key_array[i+1][0]
            
            local_checker = self.areKeysSame(key1, key2)
            
            if local_checker:
                key_array = self.changeValuesInArray(key_array, key1, key2, i, dictionary_var)
                i = 0
                    
        checker = False
    return key_array
    '''
    '''
    def changeValuesInArray(self, array, key1, key2, index, dicto):
        key1_value = array[index][1]
        key2_value = array[index+1][1]

        keyFinal = array[index][1] + array[index+1][1]

        array.pop(index)
        array.pop(index+1)
        dicto.pop(index)
        dicto.pop(index+1)

        array.append((key1, keyFinal))
        dicto.append((key1, keyFinal))

        print(dicto.most_common(5))
        return dicto.most_common(5)
    
    # Working
    def areKeysSame(self, key1, key2):
        if key1.lower() == key2.lower():
            return True
        elif key1.lower() != key2.lower():
            return False
    '''
    # def checkTopFive(self, dict):
    #     checker = True
    #     key_array = []
    #     index_storing = []
    #     boolean_storing = []
    #     while(checker):
    #         checker = False
    #         key_array = dict.most_common(5)
    #         for i in range(len(key_array)-1):
    #             key = key_array[i][0].lower()
    #             key2 = key_array[i+1][0].lower()
    #             checker = self.areKeysSame(key, i, key2, i+1, index_storing, boolean_storing)

    #         if checker == True:
    #             keyFinal = key_array[i][1] + key_array[i+1][1]
    #             key_array.pop(key_array.index((key_array[i][0], key_array[i][1])))
    #             key_array.pop(key_array.index((key_array[i+1][0], key_array[i+1][1])))
    #             key_array.append((key_array[i][0], keyFinal))
                
    #     return key_array
        
            
    
            
            
            
        
            
            

    

