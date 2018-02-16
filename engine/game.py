
import random
import string
import engine.db


MAX_CIPHER_LEN = 2
MAX_CIPHER_VAL = 10

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
                for i in range(0, MAX_CIPHER_LEN):
                    r = random.randint(0, MAX_CIPHER_VAL)
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
        
        words = ["ant", "cat", "dog", "joy", "key", "bar"]
        r = random.randint(0, len(words) - 1)
        
        return words[r]

        
            
    
    def start(self):
        
        self.ui.showIntro()
        
        while True:
        
            availableLevelIds = self.db.getAvailableLevelIds()
                  
            levelId = self.ui.chooseLevel(availableLevelIds)  
            
            level = self.db.getLevel(levelId)
                  
            self.ui.showLevelIntro(level.getId(), level.getName())
            
            
            
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
                self.db.openNextLevel(level)
            else:
                self.ui.outputLoose()


