givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

class TextAnalyzer:

    def __init__(self, text):
        text = text.lower()
        text = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        self.fmtText = text

    def freqAll(self):
        wordList = self.fmtText.split()
        freqMap = {}
        for word in set(wordList):
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self, word):
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0

analyzed = TextAnalyzer(givenstring)
print("Formatted Text:", analyzed.fmtText,"\n")

freqMap = analyzed.freqAll()
print("Frequency of all unique words:", freqMap, "\n")

searchWord = "lorem"
print(f"Frequency of {searchWord}:", analyzed.freqOf(searchWord))
        

        
