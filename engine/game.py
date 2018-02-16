
import random
import string
import engine.db
from engine.level import Level




class Game():
    
    
    def __init__(self, ui):
        self.ui = ui
        self.db = engine.db.DB()
    
    def getCipheredWord(self, word: string, rulesDict: dict) -> list:
    
        cipheredWord = []
    
        for letter in word:
            cipheredLetter = rulesDict[letter]
            cipheredWord.append(cipheredLetter)   
            
        return cipheredWord
    
     
    def createRulesDict(self, letters) -> dict: # letter-chifer
        rulesDict = {}
        
        for l in letters:
            
            while True: # until a unique cipher is found
                ruleForLetter = []
                
                cipherLen = random.randint(self.level.getMinCipherLen(), self.level.getMaxCipherLen())
                
                for i in range(0, cipherLen):
                    r = random.randint(0, self.level.getMaxCipherVal())
                    ruleForLetter.append(r)
                
                # check whether cipher already exists
                if ruleForLetter in rulesDict.values():
                    continue    
                 
                rulesDict[l] = ruleForLetter
                break;

        return rulesDict
    
    
    def getDistinctLetters(self, word: string) -> list:
        
        
        distinct = {}
        for w in word:
            distinct[w] = 0
        
        letters = []
        for key in distinct:
            letters.append(key)
   
    
        return letters
    
    
    def chooseWord(self) -> string:
        
        words = ["bee", "cat", "dog", "han", "fox", "pig", 
                 "bear", "lion", "wolf",   
                 "horse", "mouse", "tiger", 
                 "monkey", "greesly", "kangaroo", "elephant"]
        

        while True:
        
            r = random.randint(0, len(words) - 1)
            
            word = words[r]
            
            if len(word) >= self.level.getMinWordLen() and len(word) <= self.level.getMaxWordLen():    
                return word

        return ""
            
    
    def start(self):
        
        self.ui.showIntro()
        
        while True:
        
            availableLevelIds = self.db.getAvailableLevelIds()
                  
            levelId = self.ui.chooseLevel(availableLevelIds)  
            
            self.level = self.db.getLevel(levelId)
                  
            self.ui.showLevelIntro(self.level.getId(), self.level.getName())
            
            
            
            # create rulesDict
            # TODO: depends on Level! 
            while True: # until "a good mixed up" word in Rules
                word = self.chooseWord()
                letters = self.getDistinctLetters(word)
            
                rulesDict = self.createRulesDict(letters)
                
                wordInRules = ""
                for letter in rulesDict:
                    wordInRules += letter
                    
                if word != wordInRules:
                    break   
            
            cipheredWord = self.getCipheredWord(word, rulesDict)   
                 
                 
            self.ui.showField(rulesDict, cipheredWord)
                    
            guessed = self.ui.inputUserGuess()
            
                    
            if (word == guessed):
                self.ui.outputWin()
                self.db.openNextLevel(self.level)
            else:
                self.ui.outputLoose()


