import string
import pygame
import time
import engine
import ui.mainmenu

class GraphicsUI():
    
    def  __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480, 500))
        self.mainMenu = ui.mainmenu.MainMenu(self.screen)

    def showIntro(self):
        pass
        img = pygame.image.load('ui/img/intro.png')
        self.screen.blit(img, (0, 0))
        pygame.display.flip()
        time.sleep(0.2)
        
    def showMainMenu(self, levels: list) -> engine.Level:
        self.screen.fill((0,0,0))
        self.mainMenu.show(levels)
        return self.mainMenu.waitForInput()
        
        
    def showLevelIntro(self, id, name):
        pass 
    
    
    def showField(self, rulesDict, cipheredWord):
        
        self.screen.fill((0,0,0))
        
        myfont = pygame.font.SysFont('Times New Roman', 30)
        textsurface = myfont.render('Some Text', False, (255, 255, 0))
        self.screen.blit(textsurface,(50,50))
        
         
        y = 100 
        for letter in rulesDict:
            textsurface = myfont.render(letter, False, (255, 255, 0))
            self.screen.blit(textsurface,(50,y))
        
            
            x = 100
            for num in rulesDict[letter]:
                
                color = (255,215,0) # gold
                
                if num == 0: 
                    color = (204,102,51) # chocolate
                elif num == 1:
                    color = (238,130,238) # violet
                elif num == 2:
                    color = (255,235,205)  # blanched almond
                elif num == 3:
                    color = (135,206,235) # skyblue
                elif num == 4:
                    color = (255,127,80) #coral
                    
                pygame.draw.circle(self.screen, color, (x, y), 10)
                x += 30
                
            y+=30
        
        pygame.display.flip()
         
        '''        
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
        '''
            
    def inputUserGuess(self) -> string:
        guessed = input('\nType your answer: ')         
        return guessed
           