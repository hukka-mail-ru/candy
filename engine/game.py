from string import ascii_lowercase
import random
import string





class Game():
    
    def getChipheredWord(self, word, cipher):
    
        chipheredWord = []
    
        for w in word:
            chipheredLetter = []
            for num in cipher[w]:
                chipheredLetter.append(num)   
            chipheredWord.append(chipheredLetter)   
            
        return chipheredWord
     
    def getChipher(self, letters):
        ciphered = {}
        
        for l in letters:
            
            cifer = []
            for i in range(0, 3):
                r = random.randint(1, 10)
                cifer.append(r)
             
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
        
        chipheredWord = self.getChipheredWord(word, cipher)
        
        for chipheredLetter in chipheredWord:
            l = ""
            for num in chipheredLetter:
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