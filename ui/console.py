import string
import time
import pygame
import common
import sys

class ConsoleUI():
    
    
    def showIntro(self):
        print("=======================\n\n")
        print("Welcome to CANDY WORDS!\n\n")
        print("=======================\n\n")
        time.sleep(1)
        
    def showOutro(self):
        print("=======================\n\n")
        print("BYE!\n\n")
        print("=======================\n\n")
        time.sleep(1)
              
       
    def showMainMenu(self, availableLevelIds: list) -> int:
        
        print("\n====  MAIN MENU  =======\n")
        
        print("Levels: ", availableLevelIds)
        print("[E] to exit ")
         
        while True:
            choise = input('\nChoose level: ') 
            
            if(choise == "e" or choise == "E"):
                self.showOutro()
                sys.exit()
            
            for availLevId in availableLevelIds:                
                if availLevId == int(choise):                  
                    return int(choise)
                
            print("Level is not available!\n")    
        
        return 0
    
    
    def showLevelIntro(self, id, name):
              
        print("\n===== LEVEL {}: {} ======= \n".format(id, name)) 
        
    
    def showField(self, rulesDict, cipheredWord):
                

        print("Mind the rules:")
        
        for letter in rulesDict:
            rule = "  " + letter + " ... "
            for num in rulesDict[letter]:
                rule += str(chr(168 +num)) + " "
            print(rule)    
                
        print("\n")
    
        print("Guess this:")
        question = "  "
        for cipheredLetter in cipheredWord:            
            for num in cipheredLetter:
                question += str(chr(168 +num)) + " "
                                                    
        print(question)
        print("\n")
    
    
    
    def inputUserGuess(self) -> string:
        guessed = input('\nType your answer: ')         
        return guessed
    
    def outputWin(self, score: int, isHighScore: bool):
        print("=======================")
        print(" **** YOU WIN! *****")
        print(" score: ",  score)
        if isHighScore:
            print(" NEW RECORD! ")
        print("=======================\n\n")
        
    def outputLoose(self):
        print("=======================")
        print(" **** You loose! *****")
        print("=======================\n\n")

     
     
    def outputNextLevel(self):
        print("Press [N] to next level!") 
        
    def outputRetry(self):
        print("Press [R] to retry") 

    def outputMainMenu(self):
        print("Press [M] to main menu")         
        
    def inputAtFinish(self, options):
    
        if(options == common.NEXT_LEVEL):
            self.outputNextLevel()
            self.outputRetry()
            self.outputMainMenu()
            
        elif(options == common.RETRY):
            self.outputRetry()
            self.outputMainMenu()           
            
        elif(options == common.MAIN_MENU):   
            self.outputMainMenu()           
            
                         
        choise = input("Input your choise: ")
        
        if(choise == "n" or choise == "N"):
            return common.NEXT_LEVEL
                
        elif(choise == "r" or choise == "R"):     
            return common.RETRY
                
        elif(choise == "m" or choise == "M"):
            return common.MAIN_MENU