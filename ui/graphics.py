import string
import pygame
import time
import engine
import ui.mainmenu
import ui.field

class GraphicsUI():
    
    def  __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480, 500))
        self.mainMenu = ui.mainmenu.MainMenu(self.screen)
        self.field = ui.field.Field(self.screen)

    def showIntro(self):
        pass
        img = pygame.image.load('ui/img/intro.png')
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        time.sleep(0.2)
        
    def showMainMenu(self, levels: list):
        self.screen.fill((0,0,0))
        self.mainMenu.show(levels)
        
        
    def showLevelIntro(self, id, name):
        pass 
    
    
    def showField(self, rulesDict, cipheredWord):
        self.screen.fill((0,0,0))
        self.field.show(rulesDict, cipheredWord)      
         
            
    def inputUserGuess(self) -> string:
        guessed = input('\nType your answer: ')         
        return guessed