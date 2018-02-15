from string import ascii_lowercase
import random
import string

class Game():
    
    def getChipheredWord(self, word, cipher):
    
        chiphered = ""
    
        for w in word:
            chiphered += cipher[w]
            
        return chiphered
     
    def getChipher(self, letters):
        ciphered = {}
        
        for l in letters:
            
            cifer = ""
            for i in range(0, 3):
                cifer += random.choice(string.ascii_letters)
             
            ciphered[l] = cifer

    
        return ciphered
    
    def getLetters(self, word):
        
        distinct = {}
        for w in word:
            distinct[w] = 0
        
        letters = []
        for key in distinct:
            letters.append(key)
    
        return letters
    
    
    def chooseWord(self):
        
        return "hello"
    
    
    def start(self):
        
        word = self.chooseWord()
        letters = self.getLetters(word)
        cipher = self.getChipher(letters)
        
        print("cipher", cipher)
        
        chiphered = self.getChipheredWord(word, cipher)
        
        print("ciphered word", chiphered)
        
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