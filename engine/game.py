
import random
import string



MAX_CIPHER_LEN = 2
MAX_CIPHER_VAL = 10

class Game():
    
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
        
        while True: # until "a good mixed up" word in Rules
            word = self.chooseWord()
            letters = self.getDistinctLetters(word)
        
            rulesDict = self.createRulesDict(letters)
            
            wordInRules = ""
            for letter in rulesDict:
                wordInRules += letter
                
            if word != wordInRules:
                break   
        
        print("Rules:")
        for letter in rulesDict:
            print("dict", letter, rulesDict[letter])
        print("\n")
        
        
        print("Guess this!")
        cipheredWord = self.getCipheredWord(word, rulesDict)
        for cipheredLetter in cipheredWord:
            l = ""
            for num in cipheredLetter:
                l += str(num) + " "       
            print("ciphered", l)
        
        guessed = input('\ninput something!: ') 
        
        print("guessed", guessed)
        
        if (word == guessed):
            print("YES!")
        else:
            print("NO!")

if __name__ == '__main__': # pragma: no cover
    game = Game()
    
    #game.setCipher()  
    game.start()  