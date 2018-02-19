
import random
import string
import engine.db
from engine.level import Level
import common




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
                
                cipherLen = random.randint(self.level.MinCipherLen, self.level.MaxCipherLen)
                
                for i in range(0, cipherLen):
                    r = random.randint(0, self.level.MaxCipherVal)
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
            
            if len(word) >= self.level.MinWordLen and len(word) <= self.level.MaxWordLen:    
                return word

        return ""
            
    
    
    def openWin(self):
        
        self.ui.outputWin()
         
        nextLevelId = self.db.openNextLevel(self.level)
        
        
        if(nextLevelId):
            atFinish = self.ui.inputAtFinish(common.NEXT_LEVEL)
        else: 
            atFinish = self.ui.inputAtFinish(common.MAIN_MENU)
            
        
        if (atFinish == common.NEXT_LEVEL):
            self.level = self.db.getLevel(nextLevelId) 
            self.openLevel()
        elif (atFinish == common.RETRY):
            self.openLevel()
        elif (atFinish == common.MAIN_MENU):
            self.openMainMenu()   
     
     
    def openLoose(self): 
        
        self.ui.outputLoose()
        
        atFinish = self.ui.inputAtFinish(common.RETRY)   
        
        if (atFinish == common.RETRY):
            self.openLevel()
        elif (atFinish == common.MAIN_MENU):
            self.openMainMenu()   
    
    
    def openLevel(self):
        
        self.ui.showLevelIntro(self.level.Id, self.level.Name)
                                
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
            self.openWin()            
        else:            
            self.openLoose()  
    
    
    def openMainMenu(self):
        
        availableLevelIds = self.db.getAvailableLevelIds()
              
        levelId = self.ui.showMainMenu(availableLevelIds)  
        
        self.level = self.db.getLevel(levelId)   
        
        self.openLevel()
    
    
    def start(self):
        
        self.ui.showIntro()
        
        self.openMainMenu()
                  
 


