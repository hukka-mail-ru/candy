
import random
import string



MAX_CIPHER_LEN = 2
MAX_CIPHER_VAL = 10

class Game():
    
    def getCipheredWord(self, word: string, cipherDict: dict) -> list:
    
        cipheredWord = []
    
        for letter in word:
            cipheredLetter = cipherDict[letter]
            cipheredWord.append(cipheredLetter)   
            
        return cipheredWord
    
     
    def createChipherDict(self, letters) -> dict: # letter-chifer
        chipherDict = {}
        
        for l in letters:
            
            while True: # endlessly, until a unique cipher is found
                ciferForLetter = []
                for i in range(0, MAX_CIPHER_LEN):
                    r = random.randint(0, MAX_CIPHER_VAL)
                    ciferForLetter.append(r)
                
                # check whether cipher already exists
                if ciferForLetter in chipherDict.values():
                    continue    
                 
                chipherDict[l] = ciferForLetter
                break;

        return chipherDict
    
    
    def getDistinctLetters(self, word: string) -> list:
        
        distinct = {}
        for w in word:
            distinct[w] = 0
        
        letters = []
        for key in distinct:
            letters.append(key)
    
        return letters
    
    
    def chooseWord(self) -> string:
        
        return "my name is mooo"
    
    
    def start(self):
        
        word = self.chooseWord()
        letters = self.getDistinctLetters(word)
        cipherDict = self.createChipherDict(letters)
        
        print("cipherDict", cipherDict)
        
        cipheredWord = self.getCipheredWord(word, cipherDict)
        
        for cipheredLetter in cipheredWord:
            l = ""
            for num in cipheredLetter:
                l += str(num) + " "       
            print("ciphered", l)
        
        guessed = input('input something!: ') 
        
        print("guessed", guessed)
        
        if (word == guessed):
            print("YES!")
        else:
            print("NO!")

if __name__ == '__main__': # pragma: no cover
    game = Game()
    
    #game.setCipher()  
    game.start()  