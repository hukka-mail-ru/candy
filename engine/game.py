
import random
import string
import engine.db
import common
import time




class Game():
    
    def __init__(self):
        self.db = engine.db.DB()   
        self._readWordsFromFile()
       
    def setUI(self, ui):    
        self.ui = ui
    
        
    def start(self):
        
        self.ui.showIntro()
        
        self._openMainMenu()
                  
    
    def startLevel(self, level):
        
        print("Starting level ", level.Id, level.Name)

        self.level = level
        
        
        self.ui.showLevelIntro(self.level.Id, self.level.Name)
                                
        # create rulesDict
        word = self._chooseWord()
        
        if(word == ""):
            self._readWordsFromFile()
            word = self._chooseWord()

        
        letters = self._getDistinctLetters(word)    
        rulesDict = self._createRulesDict(letters)
        
        
        cipheredWord = self._getCipheredWord(word, rulesDict)   
                          
        self.ui.showField(rulesDict, cipheredWord)
        
        
        start = time.time()                
        guessed = self.ui.inputUserGuess()            
        end = time.time()
        
        
        
        score = self.level.Id * len(word) / (end - start) * 1000      
                
        if (word == guessed):
            self._openWin(int(score))            
        else:            
            self._openLoose()  
        
        
    def _readWordsFromFile(self):
        
        self.words = [] 
        with open('engine/words.txt','r') as f:
            for line in f:
                for word in line.split():
                    self.words.append(word)      
                    
                    
    
    def _getCipheredWord(self, word: string, rulesDict: dict) -> list:
    
        cipheredWord = []
    
        for letter in word:
            cipheredLetter = rulesDict[letter]
            cipheredWord.append(cipheredLetter)   
            
        return cipheredWord
    
     
    def _createRulesDict(self, letters) -> dict: # letter-chifer
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
    
    
    def _getDistinctLetters(self, word: string) -> list:
        
        
        distinct = {}
        for w in word:
            distinct[w] = 0
        
        letters = []
        for key in distinct:
            letters.append(key)
   
    
        return letters
    
    
    def _chooseWord(self) -> string:
        
        random.seed()
        
        wordsForThisLevel = []
        for word in self.words:
            if len(word) >= self.level.MinWordLen and len(word) <= self.level.MaxWordLen:
                wordsForThisLevel.append(word)
        
        if len(wordsForThisLevel) < 1:
            return ""       
        
        r = random.randint(0, len(wordsForThisLevel) - 1)
        word = wordsForThisLevel[r]
        self.words.remove(word)   
              
        return word

            
    
    
    def _openWin(self, score: int):
        
        isHighScore = self.db.isHighScore(self.level, score)
                    
        self.ui.outputWin(score, isHighScore)
         
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
            self._openMainMenu()   
     
     
    def _openLoose(self): 
        
        self.ui.outputLoose()
        
        atFinish = self.ui.inputAtFinish(common.RETRY)   
        
        if (atFinish == common.RETRY):
            self.openLevel()
        elif (atFinish == common.MAIN_MENU):
            self._openMainMenu()   
   
    

    
    
    def _openMainMenu(self):
        
        levels = self.db.getLevels()
              
        self.ui.showMainMenu(levels)  
     

    

 


