import string
import time

class ConsoleUI():
    
    
    def showIntro(self):
        print("=======================\n\n")
        print("Welcome to CANDY WORDS!\n\n")
        print("=======================\n\n")
        time.sleep(1)
        
        
       
    def chooseLevel(self, availableLevels: list):
        print("Levels: ", availableLevels)
        
        while True:
            levelId = input('\nChoose level: ') 
            
            for availLev in availableLevels:
                
                (availId, availName) = availLev
                if availId == int(levelId):
                    self.level = availLev                    
                    return
                
            print("Level is not available!\n")    
        
        return 0
    
    
    def showLevelIntro(self):
        
        (id, name) = self.level
        
        print("\nStarting Level {}: {}\n".format(id, name)) 
        
    
    def showField(self, rulesDict, cipheredWord):
                

        print("Rules:")
        for letter in rulesDict:
            print("dict", letter, rulesDict[letter])
        print("\n")
    
        print("Guess this!")
        for cipheredLetter in cipheredWord:
            l = ""
            for num in cipheredLetter:
                l += str(num) + " "       
            print("ciphered", l)
    
    
    
    
    def inputUserGuess(self) -> string:
        guessed = input('\ninput something!: ')         
        print("guessed", guessed)
        return guessed
    
    def outputWin(self):
        print("You win!")
        
    def outputLoose(self):
        print("You loose!")