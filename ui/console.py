import string
import time
import pygame

class ConsoleUI():
    
    
    def showIntro(self):
        print("=======================\n\n")
        print("Welcome to CANDY WORDS!\n\n")
        print("=======================\n\n")
        time.sleep(1)
        
        
       
    def chooseLevel(self, availableLevelIds: list) -> int:
        print("Levels: ", availableLevelIds)
        
        while True:
            levelId = input('\nChoose level: ') 
            
            for availLevId in availableLevelIds:                
                if availLevId == int(levelId):                  
                    return int(levelId)
                
            print("Level is not available!\n")    
        
        return 0
    
    
    def showLevelIntro(self, id, name):
                    
        print("\nStarting Level {}: {}\n".format(id, name)) 
        
    
    def showField(self, rulesDict, cipheredWord):
                

        print("Mind the rules:")
        for letter in rulesDict:
            print("  {} ... {} ".format(letter, rulesDict[letter]))
        print("\n")
    
        print("Guess this:")
        question = "  "
        for cipheredLetter in cipheredWord:            
            for num in cipheredLetter:
                question += str(num) + " "
                                                    
        print(question)
        print("\n")
    
    def waitForKey(self):        
        input("Press enter to continue")
    
    
    def inputUserGuess(self) -> string:
        guessed = input('\nType your answer: ')         
        return guessed
    
    def outputWin(self):
        print("\n")
        print(" **** You win! *****")
        print("=======================\n\n")
        self.waitForKey()
        print("\n\n\n")
        
    def outputLoose(self):
        print("You loose!")
        print("=======================\n\n")
        self.waitForKey()
        print("\n\n\n")